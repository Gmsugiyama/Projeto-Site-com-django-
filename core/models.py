import uuid
from django.db import models
from stdimage.models import StdImageField


def get_file_path(_instance, filename):
    ext = filename.split('.')[-1]
    filename = f'{uuid.uuid4()}.{ext}'
    return filename


class Base(models.Model):
    criados = models.DateField('Criação', auto_now_add=True)
    modificado = models.DateField('Modificado', auto_now=True)
    ativo = models.BooleanField('Ativo?', default=True)

    class Meta:
        abstract = True


class Servicos(Base):
    ICONE_CHOICES = (
        ('lni-cog', 'engrenagem'),
        ('lni-stats-up', 'gráficos'),
        ('lni-user', 'usuários'),
        ('lni-layers', 'design'),
        ('lni-mobile', 'mobile'),
        ('lni-rocket', 'foguete'),
    )
    servico = models.CharField('Serviços', max_length=100)
    descricao = models.TextField('Descrição', max_length=200)
    icone = models.CharField('Icone', max_length=12, choices=ICONE_CHOICES)

    class Meta:
        verbose_name = 'Serviço'
        verbose_name_plural = 'Serviços'

    def __str__(self):
        return self.servico


class Cargo(Base):
    cargo = models.CharField('cargo', max_length=100)

    class Meta:
        verbose_name = 'Cargo'
        verbose_name_plural = 'Cargos'

    def __str__(self):
        return self.cargo


class Funcionario(Base):
    nome = models.CharField('nome', max_length=100)
    cargo = models.ForeignKey('core.Cargo', verbose_name='Cargo', on_delete=models.CASCADE)
    bio = models.TextField('Bio', max_length=400)
    imagem = StdImageField('imagem', upload_to=get_file_path, variations={'thumb': {'width': 480, 'height': 480, 'crop': True}})
    facebook = models.CharField('Facebook', max_length=100, default='--')
    instragram = models.CharField('Instagram', max_length=100, default='--')
    twitter = models.CharField('Twitter', max_length=100, default='--')

    class Meta:
        verbose_name = 'Funcionário'
        verbose_name_plural = 'Funcionários'

    def __str__(self):
        return self.nome


class Recurso(Base):
    ICONE_CHOICES = (
        ('lni-cog', 'engrenagem'),
        ('lni-leaf', 'folha'),
        ('lni-layers', 'design'),
        ('lni-laptop-phone', 'laptop'),
        ('lni-rocket', 'foguete'),
    )
    RECURSOS_CHOICES = (
        ('box-item wow fadeInLeft', 'esquerda'),
        ('box-item wow fadeInRight', 'direita'),
    )
    DELAY_CHOICES = (
        ('0.3s', '0.3'),
        ('0.6s', '0.6'),
        ('0.9s', '0.9'),
    )
    nome = models.CharField('nome', max_length=100)
    icone = StdImageField('icone', max_length=17, choices=ICONE_CHOICES)
    texto = models.CharField('texto', max_length=200)
    posicao = models.CharField('posicionamento', max_length=24, choices=RECURSOS_CHOICES, default=True)
    delay_p = models.CharField('delay-posição', max_length=4, choices=DELAY_CHOICES, default=True)

    class Meta:
        verbose_name = 'recurso'
        verbose_name_plural = 'recursos'

    def __str__(self):
        return self.nome

