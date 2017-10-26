from django.db import models


class Category(models.Model):
    title = models.CharField('title', max_length=100)
    slug = models.SlugField('slug', unique=True)

    class Meta:
        verbose_name = 'category'
        verbose_name_plural = 'categories'
        db_table = 'categories'
        ordering = ('title',)

    def __unicode__(self):
        return u'%s' % self.title


class Client(models.Model):
    name = models.CharField(max_length=100)
    slug = models.SlugField(unique=True)
    url = models.URLField()

    class Meta:
        db_table = 'clients'
        ordering = ('name', )

    def __unicode__(self):
        return self.name


class ProjectImage(models.Model):
    title = models.CharField(max_length=255)
    slug = models.SlugField()
    image_path = models.CharField(max_length=100, blank=True)
    image = models.FileField(upload_to="images/portfolio", blank=True)
    credit = models.CharField(max_length=100, blank=True)
    description = models.TextField(blank=True)
    # tags = TaggableManager()
    is_featured = models.BooleanField('Is this image featured on your main pages?', blank=None)
    uploaded = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = 'project_images'

    def __unicode__(self):
        return '%s' % self.title

    def get_absolute_url(self):
        return self.slug


class Project(models.Model):

    name = models.CharField(max_length=250)
    slug = models.SlugField()
    project_url = models.URLField('Project URL')
    type = models.ManyToManyField(Category, blank=True)
    description = models.TextField(blank=True)
    client = models.ForeignKey(Client)
    completion_date = models.DateField()
    in_development = models.BooleanField(default=False)
    is_public = models.BooleanField(default=True)
    #images = models.ManyToManyField(ProjectImage)
    image = models.FileField(upload_to="images/portfolio", blank=True)
    is_featured = models.BooleanField(default=False)

    class Meta:
        db_table = 'projects'
        ordering = ('-completion_date',)

    def __unicode__(self):
        return self.name

    def get_absolute_url(self):
        return "/work/%s/" % self.slug
