import logging

from copy import deepcopy
from functools import reduce

from django.contrib.auth.models import Group, Permission
from django.contrib.contenttypes.models import ContentType
from rest_framework import serializers

from staff.models import Part
from .models import ContentTypeCat, ContentTypeCatRel

logger = logging.getLogger(__name__)

class ContentTypeCatRelSerializer(serializers.ModelSerializer):

  
    class Meta:
        model = ContentTypeCatRel
        fields = '__all__'


class ContentTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = ContentType
        fields = '__all__'


class PermissionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Permission
        fields = ('name', 'content_type', 'codename')


class ContentTypeCatSerializer(serializers.ModelSerializer):
    # content_type_cat_rels = serializers.SerializerMethodField()

    # def get_content_type_cat_rels(self, obj):
    #     """
    #     获取当前组可以操作的content_type_cat_rels
    #     """

    #     content_type_cat_rels = obj.contenttypecatrel_set.all()

    #     return ContentTypeCatRelSerializer(content_type_cat_rels, many=True).data


    class Meta:
        model = ContentTypeCat
        fields = '__all__'


class GroupSerializer(serializers.ModelSerializer):

    content_type_cats_serializer = serializers.SerializerMethodField()
    # content_types_serializer = serializers.SerializerMethodField()
    content_type_cat_rels_serializer = serializers.SerializerMethodField()
    permissions_serializer = serializers.SerializerMethodField()

    def get_content_types(self, obj):
        content_type_ids = list(map(
            lambda perm: perm.content_type_id, obj.permissions.all()))
        return ContentType.objects.filter(id__in=content_type_ids).distinct().all()

    # def get_content_type_cat_rels(self, obj):
    #     content_types = self.get_content_types(obj)
    #     content_type_cat_rels = map(
    #         lambda ct: ct.content_type_cat_rel, content_types)
    #     return content_type_cat_rels

    def get_content_type_cat_rels(self, obj):
        # 得到所有的二级菜单
        content_types = self.get_content_types(obj)
        content_type_cat_rels = map(
            lambda ct: list(ct.content_type_cat_rel.all()), content_types)
        content_type_cat_rels = reduce(lambda a, b: a + b, content_type_cat_rels)

        # 删除有重复的二级菜单
        b = []
        for i in content_type_cat_rels:
            if i.name not in b:
                b.append(i.name)

            else:
                content_type_cat_rels.remove(i)

        return content_type_cat_rels

    def get_content_type_cats(self, obj):
        """
        获取当前组可以操作的content_type_cat
        """
        content_type_cat_rels = self.get_content_type_cat_rels(obj)

        content_type_cats = map(
            lambda ctcr: ctcr.content_type_cat, content_type_cat_rels)
        return list(set(content_type_cats))

    def get_content_types_serializer(self, obj):
        """
        获取当前group可操作的资源
        """
        content_types = self.get_content_types(obj)
        return ContentTypeSerializer(content_types, many=True).data

    def get_content_type_cat_rels_serializer(self, obj):
        """
        获取当前组可以操作的content_type_cat_rels
        """
        # 删除没有二级菜单的一级菜单下的二级菜单，哪些是在数据库中联系一级菜单而又不用更改代码使用的，返回给前端没有用，所以删除
        content_type_cat_rels = self.get_content_type_cat_rels(obj)
        content_type_cat_rels_list = list(deepcopy(content_type_cat_rels))
        for c in content_type_cat_rels:
            # 判断其一级菜单是否拥有二级菜单
            if not c.content_type_cat.has_sub:
                content_type_cat_rels_list.remove(c)

        # part_id = self.context.get("user").default_part_id
        # part = Part.objects.get(id=part_id)
        # # 判断工区是普通工区还是桥隧
        # b = ContentTypeCat.objects.get(id = 3)
        # if part.status:
        #     content_type_cat_rels_list.remove(b)

        return ContentTypeCatRelSerializer(content_type_cat_rels_list, many=True).data

    def get_content_type_cats_serializer(self, obj):
        """
        获取当前组可以操作的content_type_cat
        """

        content_type_cats = self.get_content_type_cats(obj)
        content_type_cat_rels = self.get_content_type_cat_rels(obj)
        content_type_cats_list = list(deepcopy(content_type_cats))

        # for ctc in content_type_cats:
        #     # ctcrs = filter(lambda ctr : ctr.content_type_cat_id == ctc.id,content_type_cat_rels)
        #     ctc.contenttypecatrel_set.set([ContentTypeCatRel.objects.get(id=1)])

        # part_id = self.context.get("user").default_part_id
        # part = Part.objects.get(id=part_id)
        # # 判断工区是普通工区还是桥隧
        # b = ContentTypeCat.objects.get(id = 3)
        # if part.status:
        #     content_type_cats_list.remove(b)

        ret = ContentTypeCatSerializer(content_type_cats_list, many=True)

        return ret.data

    def get_permissions_serializer(self, obj):
        return PermissionSerializer(obj.permissions, many=True).data

    class Meta:
        model = Group
        fields = '__all__'


