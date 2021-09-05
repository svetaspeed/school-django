from django.db import models


# class Picture(models.Model):
#     local_url = models.ImageField(upload_to=upload_to)
#     url_to_upload = models.CharField(max_length=200, default='')
#
#     @staticmethod
#     def upload_image(owner, owner_type, picture_type, image, base=""):
#         image_name = Picture.get_uuid_name_with_extension(image)
#         picture = Picture.objects.create(
#             local_url=image,
#             url_to_upload=Uploader.get_path(owner, owner_type, picture_type, image_name, base_for_file=base))
#         return picture
#
#     def delete(self, using=None, keep_parents=False):
#         os.remove(self.url_to_upload)
#         super().delete(using=using, keep_parents=keep_parents)


class News(models.Model):
    title = models.CharField('Заголовок', max_length=50)
    text = models.TextField('Текст')
    # image = models.ForeignKey(Picture, on_delete=models.SET_NULL, null=True)
    # image = models.ImageField(upload_to='./media/news', height_field=100, width_field=100)


    # def set_image(self, image):
    #     if self.image is not None:
    #         self.image.delete()
    #     self.image = Picture.upload_image(owner=self.title.id, image=image, owner_type='title',
    #                                       picture_type='news', base=self.id)
    #     self.save()

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Новость'
        verbose_name_plural = 'Новости'
