from rest_framework import status
from rest_framework.permissions import IsAdminUser, IsAuthenticated
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet

from orders.models import Order
from orders.serializers import OrderListSerializer
from products.models import Basket


class OrderModelViewSet(ModelViewSet):
    serializer_class = OrderListSerializer
    queryset = Order.objects.all()

    def get_queryset(self):
        queryset = super(OrderModelViewSet, self).get_queryset()
        return queryset.filter(initiator=self.request.user)

    def create(self, request, *args, **kwargs):

        try:
            baskets = Basket.objects.filter(user=self.request.user)
            if not baskets:
                return Response({'basket': 'basket empty'}, status=status.HTTP_400_BAD_REQUEST)
            order = Order.objects.create(first_name=self.request.data['first_name'],
                                         last_name=self.request.data['last_name'],
                                         email=self.request.data['email'], address=self.request.data['address'],
                                         zipcode=self.request.data['zipcode'], telephone=self.request.data['telephone'],
                                         basket_history=[basket.de_json() for basket in baskets],
                                         initiator=self.request.user, )
            serializer = self.get_serializer(order)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        except KeyError:
            return Response({'Error': 'Error'}, status=status.HTTP_400_BAD_REQUEST)

    def get_permissions(self):
        if self.action in ('create', 'list'):
            self.permission_classes = (IsAuthenticated,)
        else:
            self.permission_classes = (IsAdminUser,)
        return super(OrderModelViewSet, self).get_permissions()
