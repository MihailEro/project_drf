from rest_framework import serializers

from course.models import Course, Subscribe

from lessons.serializers import LessonSerializers
from payments.models import Payment
from payments.services import create_payment_intent, retrieve_payment_intent


class CourseSerializer(serializers.ModelSerializer):
    lessons_count = serializers.SerializerMethodField(read_only=True)
    lessons = LessonSerializers(many=True, read_only=True)
    subscribe = serializers.SerializerMethodField(read_only=True)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.request = kwargs.get('context').get('request')

    @staticmethod
    def get_lesson_count(instance):
        return instance.lessons.count()

    def get_is_subscribe(self, instance):
        subs = Subscribe.objects.filter(user=self.request.user, course=instance).first()

        if subs and subs.is_active:
            return True
        else:
            return False

    class Meta:
        model = Course
        fields = '__all__'


class SubscribeSerializer(serializers.ModelSerializer):

    class Meta:
        model = Subscribe
        fields = '__all__'


class PaymentSerializer(serializers.ModelSerializer):

    class Meta:
        model = Payment
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.request = kwargs.get('context').get('request')

    def gett_payment_stripe(self, instance):
        if self.request.method == 'POST':
            pay_id = create_payment_intent(instance.amount)
            obj = Payment.objects.get(id=instance.id)
            obj.pay_id = pay_id
            obj.save()

            return retrieve_payment_intent(pay_id)
