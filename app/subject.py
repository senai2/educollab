from django.contrib.auth import login, authenticate
from django.contrib.auth.models import User
from django.shortcuts import render, redirect, get_object_or_404
from .utils import check_user_id
from app.models import Member, ChangeLog, Subscription, Subject
from educollab import settings


def showsubject(request, sid):
    subject = get_object_or_404(Subject, id=sid)

    user_subscription = Subscription.objects.filter(
        member=request.user.id, subject=subject, curriculum__isnull=True).exclude(subject__isnull=True)

    if request.method == 'GET':

        if user_subscription:
            button_status = 'Unsubscribe'
        else:
            button_status = 'Subscribe'

        context = {
            'subject': subject,
            'button_status': button_status,
        }
        return render(request, 'subject.html', context)

    if request.method == 'POST':
        """
        Filtering user subscription by only
        allowing records with subjects not
        being NULL and curriculums being NULL

        """
        if user_subscription:
            user_subscription.delete()

            # Updating Change Log for the change
            reason = 'Unsubscribed from Subject' + \
                str(sid) + '+ more details'
            log_obj = ChangeLog(
                member=Member(id=request.user.id),
                description=reason,
                curriculum=None,
                bit=None,
                subject=subject,
            )
            log_obj.save()

            sub_status = 'Unsubscribed!'
            button_status = 'Subscribe'

        else:
            sub_obj = Subscription(
                member=Member(id=request.user.id),
                subject=subject,
                curriculum=None
            )
            sub_obj.save()

            # Updating Change Log for the change
            reason = 'Subscribed to Curriculum' + \
                str(sid) + '+ more details'
            log_obj = ChangeLog(
                member=Member(id=request.user.id),
                description=reason,
                curriculum=None,
                bit=None,
                subject=subject,
            )
            log_obj.save()

            sub_status = 'Subscribed!'
            button_status = 'Unsubscribe'

        context = {'subject': subject,
                   'sub_status': sub_status,
                   'button_status': button_status}
        return render(request, 'subject.html', context)
