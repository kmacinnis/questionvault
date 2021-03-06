from django.db import models
from django.contrib.auth.models import User
from django.core.urlresolvers import reverse
import picklefield
from questions.models import Question


class Exercise(models.Model):
    question = models.ForeignKey(Question, db_index=True)
    vardict = picklefield.PickledObjectField()
    def __str__(self):
        return "Exercise «{0}»".format(self.id)


class DocumentRecipe(models.Model):
    title = models.CharField(max_length=60)
    created_by = models.ForeignKey(User)
    date_created = models.DateField(auto_now_add=True)
    public = models.BooleanField(default=False)
    def __str__(self):
        return self.title
    def get_absolute_url(self):
        return reverse('EditDocRecipe', args=[str(self.id)])


class BlockRecipe(models.Model):
    '''
    A block is a set of exercises created from the same question.
    '''
    document = models.ForeignKey(DocumentRecipe)
    order = models.IntegerField(default=999)
    question = models.ForeignKey(Question, db_index=True)
    num_exercises = models.IntegerField()
    num_columns = models.IntegerField(default=1)
    space_after = models.CharField(max_length=30)
    class Meta:
        ordering = ['order']
    def __str__(self):
        return 'Block {order} of {doc}'.format(
                    order=self.order, doc=self.document.title)


class Document(models.Model):
    title = models.CharField(max_length=60)
    recipe = models.ForeignKey(DocumentRecipe)
    date_created = models.DateTimeField(auto_now_add=True)
    created_by = models.ForeignKey(User)
    public = models.BooleanField(default=False)
    def __str__(self):
        return self.title


class Block(models.Model):
    document = models.ForeignKey(Document)
    order = models.IntegerField()
    recipe = models.ForeignKey(BlockRecipe)
    exercises = models.ManyToManyField(Exercise)
    
    @property
    def num_columns(self):
        return self.recipe.num_columns
    
    @property
    def prompt(self):
        return self.recipe.question.prompt
    
    @property
    def space_after(self):
        return self.recipe.space_after
        









