from django.shortcuts import render

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.shortcuts import get_object_or_404
from drf_yasg.utils import swagger_auto_schema
from django_app.serializers import *


class CustomerAPI ( APIView ) :
    @swagger_auto_schema ( request_body=CustomerSerializer )
    def post(self, request) :
        serializer = CustomerSerializer ( data=request.data )
        serializer.is_valid ( raise_exception=True )
        serializer.save ()
        return Response ( data=serializer.data, status=status.HTTP_201_CREATED )

    def get(self, request) :
        customers = Customer.objects.all ()
        serializer = CustomerSerializer ( customers, many=True )
        return Response ( data=serializer.data, status=status.HTTP_200_OK )


class CustomerDetailAPI ( APIView ) :
    def get(self, request, slug) :
        customer = get_object_or_404 ( Customer, slug=slug )
        serializer = CustomerSerializer ( customer )
        return Response ( data=serializer.data, status=status.HTTP_200_OK )

    def put(self, request, slug) :
        customer = get_object_or_404 ( Customer, slug=slug )
        serializer = CustomerSerializer ( customer, data=request.data, partial=True )
        serializer.is_valid ( raise_exception=True )
        serializer.save ()
        return Response ( data=serializer.data, status=status.HTTP_200_OK )

    def delete(self, request, slug) :
        customer = get_object_or_404 ( Customer, slug=slug )
        customer.delete ()
        return Response ( status=status.HTTP_204_NO_CONTENT )


class EmployeeAPI ( APIView ) :
    @swagger_auto_schema ( request_body=EmployeeSerializer )
    def post(self, request) :
        serializer = EmployeeSerializer ( data=request.data )
        serializer.is_valid ( raise_exception=True )
        serializer.save ()
        return Response ( data=serializer.data, status=status.HTTP_201_CREATED )

    def get(self, request) :
        employees = Employee.objects.all ()
        serializer = EmployeeSerializer ( employees, many=True )
        return Response ( data=serializer.data, status=status.HTTP_200_OK )


class EmployeeDetailAPI ( APIView ) :
    def get(self, request, slug) :
        employee = get_object_or_404 ( Employee, slug=slug )
        serializer = EmployeeSerializer ( employee )
        return Response ( data=serializer.data, status=status.HTTP_200_OK )

    def put(self, request, slug) :
        employee = get_object_or_404 ( Employee, slug=slug )
        serializer = EmployeeSerializer ( employee, data=request.data, partial=True )
        serializer.is_valid ( raise_exception=True )
        serializer.save ()
        return Response ( data=serializer.data, status=status.HTTP_200_OK )

    def delete(self, request, slug) :
        employee = get_object_or_404 ( Employee, slug=slug )
        employee.delete ()
        return Response ( status=status.HTTP_204_NO_CONTENT )


class OrderAPI ( APIView ) :
    @swagger_auto_schema ( request_body=OrderSerializer )
    def post(self, request) :
        serializer = OrderSerializer ( data=request.data )
        serializer.is_valid ( raise_exception=True )
        serializer.save ()
        return Response ( data=serializer.data, status=status.HTTP_201_CREATED )

    def get(self, request) :
        orders = Order.objects.all ()
        serializer = OrderSerializer ( orders, many=True )
        return Response ( data=serializer.data, status=status.HTTP_200_OK )


class OrderDetailAPI ( APIView ) :
    def get(self, request, slug) :
        order = get_object_or_404 ( Order, slug=slug )
        serializer = OrderSerializer ( order )
        return Response ( data=serializer.data, status=status.HTTP_200_OK )

    def put(self, request, slug) :
        order = get_object_or_404 ( Order, slug=slug )
        serializer = OrderSerializer ( order, data=request.data, partial=True )
        serializer.is_valid ( raise_exception=True )
        serializer.save ()
        return Response ( data=serializer.data, status=status.HTTP_200_OK )

    def delete(self, request, slug) :
        order = get_object_or_404 ( Order, slug=slug )
        order.delete ()
        return Response ( status=status.HTTP_204_NO_CONTENT )