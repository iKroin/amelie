import datetime

from django.db import models
from django.db.models import Q
from django.utils import timezone

from amelie.tools.logic import current_association_year, association_year


class PersonManager(models.Manager):
    def members(self):
        return super(PersonManager, self).get_queryset().filter(
            Q(membership__year=current_association_year()),
            Q(membership__ended__isnull=True) | Q(membership__ended__gt=datetime.date.today())
        )

    def active_members(self):
        return self.members().filter(function__begin__isnull=False, function__end__isnull=True,
                                     function__committee__abolished__isnull=True).distinct()

    def board(self):
        # Import here because of circular imports
        from amelie.members.models import Committee

        return self.active_members().filter(function__committee=Committee.objects.get(abbreviation="Bestuur"),
                                            function__end__isnull=True)

    def current_or_grace_period_membership(self):
        half_year_ago = timezone.now() - datetime.timedelta(days=180)

        return self.filter(
            Q(membership__ended__isnull=True) | Q(membership__ended__gte=half_year_ago),
            membership__year__gte=association_year(half_year_ago)
        )


class CommitteeManager(models.Manager):
    """
    ModelManager that only shows the non-parent committees
    """

    def non_parent_committees(self):
        return super(CommitteeManager, self).get_queryset().filter(committee__isnull=True)

    # TODO: Was get_queryset().filter(..). Did not work that well on sub-sub queries -- zeilstraj 19-02-2015
    # Should work fine, but I'm not sure -- stottelaarb 31-12-2011
    def active(self):
        return super(CommitteeManager, self).filter(abolished__isnull=True)
