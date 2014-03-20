# -*- coding: utf-8 -*-
from django.core.management.base import BaseCommand, CommandError
from django.db import transaction
from django.db.utils import IntegrityError
from django.utils.encoding import DjangoUnicodeDecodeError

import dateutil.parser

from transaction_log.models import Transaction
from room.models import Device
import csv

class Command(BaseCommand):
    args ='<filename>'
    help = 'Upload Transaction log'
    def handle(self, *args, **options):
        reader = csv.reader(open(args[0], "rb"))
        i=0
        try :
            for tx in reader:
                try:
                    i=i+1
                    t=Transaction.objects.create(
                        username = unicode(tx[0]),
                        timestamp = dateutil.parser.parse(unicode(tx[1])),
                        device = Device.objects.get(fac_id=unicode(tx[2])),
                        )
                    self.stdout.write('%s : Successfully upload transacton "%s"\n' % (i,t))

                except IntegrityError:
                    print 'TX "%s" failure, duplicate transactions' % i

                except DjangoUnicodeDecodeError, e:
                    print "error line %s : %s ---\n %s" % (i,tx,e)

                #except exception:
                #    raise CommandError('TX "%s" failure : %s' % args[0],e)
        except Exception,e:
            print "ERROR : %s" % e
