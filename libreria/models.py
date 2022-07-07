from distutils.command.upload import upload
from xmlrpc.client import boolean
from django.db import models
from django.utils.html import format_html
from django.utils import timezone

# Create your models here.
class Departamentos(models.Model):
    id_departamento = models.AutoField(primary_key=True)
    nombre_departamento = models.CharField(max_length=30, verbose_name="Nombre Departamento" ,null=True)
    estado_departamento = models.BooleanField(default='1')
    
    def nombre_departamentos(self):
        return "{}".format(self.nombre_departamento)
    def __str__(self):
        return self.nombre_departamentos()
    class Meta:
        verbose_name='Departamento'
        verbose_name_plural='Departamentos'
        db_table='departamentos'
        ordering=['nombre_departamento']


class Provincias(models.Model):
    id_provincia = models.AutoField(primary_key=True)
    nombre_provincia = models.CharField(max_length=30, verbose_name="Nombre Provincia" ,null=True)
    departamento=models.ForeignKey(Departamentos,null=True,blank=True,on_delete=models.CASCADE)
    estado_provincia = models.BooleanField(default='1')
    
    def nombre_provincias(self):
        return "{}".format(self.nombre_provincia)
    def __str__(self):
        return self.nombre_provincias()
    class Meta:
        verbose_name='Provincia'
        verbose_name_plural='Provincias'
        db_table='provincias'
        #ordering=['nombre_provincia']

class Ilcs(models.Model):
    id_ilc=models.AutoField(primary_key=True)
    departamento=models.ForeignKey(Departamentos,null=True,blank=True,on_delete=models.CASCADE)
    imagen = models.ImageField(upload_to='imagenes/', verbose_name="Imagen" ,null=True)
    ilc = models.CharField(max_length=50, verbose_name="Ilc" ,null=True)
    nacion = models.CharField(max_length=50, verbose_name="Nación" ,null=True)
    idioma = models.CharField(max_length=50, verbose_name="Idioma" ,null=True)
    region = models.CharField(max_length=50, verbose_name="Region" ,null=True)
    estado_ilc = models.BooleanField(default='1',verbose_name="Activo")

    def __str__(self):
        fila =self.ilc + " , " + self.nacion + " , " + "Idioma: " + self.idioma
        return fila
    def delete(self, using=None, keep_parents=False):
        self.imagen.storage.delete(self.imagen.name)
        super().delete()
    class Meta:
        verbose_name='Ilc'
        verbose_name_plural='Ilcs'
        db_table='ilcs'
        ordering=['idioma']

class Coordinaciones(models.Model):
    #id_coordinacion = models.AutoField(primary_key=True)
    nombre_coordinacion = models.CharField(max_length=50, verbose_name="Nombre Coordinación" , blank=False)
    nombre_corto = models.CharField(max_length=10, verbose_name='SLUG', blank=True)
    estado_coordinacion = models.BooleanField(default='1')
    
    def nombre_coordinaciones(self):
        return "{} - {}".format(self.nombre_coordinacion, self.nombre_corto)
    def __str__(self):
        return self.nombre_coordinaciones()
    class Meta:
        verbose_name='Coordinacion'
        verbose_name_plural='Coordinaciones'
        db_table='coordinaciones'
        ordering=['nombre_coordinacion']

class ObjetivosEstrategicos(models.Model):
    nombre_objetivo = models.CharField(max_length=100, verbose_name="Objetivo Estratégico" ,null=True)
    coordinacion=models.ForeignKey(Coordinaciones,null=True,blank=True,verbose_name="Coordinacion ",on_delete=models.CASCADE)
    estado_objetivo = models.BooleanField(default='1')
    
    def nombre_objetivos(self):
        return "{}".format(self.nombre_objetivo)
    def __str__(self):
        return self.nombre_objetivos()
    class Meta:
        verbose_name='Objetivo'
        verbose_name_plural='Objetivos'
        db_table='objetivos'
        ordering=['nombre_objetivo']

class Funcionarios(models.Model):
    nrodocumento = models.PositiveIntegerField(verbose_name='Nro de Documento')
    extension = models.CharField(max_length=2, verbose_name='Extensión', blank=True)
    nombres = models.CharField(max_length=50, verbose_name='Nombres',blank=False)
    primerapellido = models.CharField(max_length=40, verbose_name='Primer Apellido',blank=True)
    segundoapellido = models.CharField(max_length=40, verbose_name='Segundo apellido',blank=False)
    email = models.EmailField(verbose_name='Email',blank=True)
    fechaCumpleanos = models.DateField(blank=True, null=True, verbose_name='Fecha Nacimiento')
    fechaIngreso = models.DateField(blank=True, null=True, verbose_name='Fecha de ingreso')
    nroItem = models.PositiveIntegerField(verbose_name='Numero de ITEM', blank=False)
    codUnidEducativa = models.PositiveIntegerField(verbose_name='Código Unidad Educativa', blank=False)
    nroServicio = models.PositiveIntegerField(verbose_name='Número de Servicio',blank=False)

    def nombre_funcionarios(self):
        return "{} - {} {} {}".format(self.nrodocumento, self.nombres, self.primerapellido, self.segundoapellido)
    def __str__(self):
        return self.nombre_funcionarios()
    class Meta:
        verbose_name='Funcionario'
        verbose_name_plural='Funcionarios'
        db_table='funcionarios'
        ordering=['primerapellido']


class Actividades(models.Model):
    nombre_actividad = models.CharField(max_length=100, verbose_name='Nombre de la Actividad')
    coordinacion=models.ForeignKey(Coordinaciones,null=True,blank=True,verbose_name='Cordinación con unidad del IPELC',on_delete=models.CASCADE)
    objetivo_estrategico=models.ForeignKey(ObjetivosEstrategicos,null=True,blank=True,verbose_name='Objetivo Estrategico',on_delete=models.CASCADE)
    lugar_actividad = models.CharField(max_length=50, verbose_name='Lugar de la Actividad')
    cantidad_dias = models.PositiveIntegerField(verbose_name='Cantidad de Dias')
    fechainicio = models.DateTimeField(default=timezone.now,verbose_name='Fecha y hora de la Actividad' )
    observacion = models.TextField(max_length=200, verbose_name='Observacion', null=True)
    archivo = models.FileField(upload_to='files/', verbose_name="Adjuntar en pdf Planificacion" ,null=True,)
    def actividad_detalle(self):
        return "Actividad: {}, Lugar: {}". format(self.nombre_actividad,self.lugar_actividad)
    def __str__(self):
        return self.actividad_detalle()
    def filename(self): return os.path.basename(self.file.archivo,self.primerapellido)
    class Meta:
        verbose_name='Actividad'
        verbose_name_plural='Actividades'
        db_table='actividades'
         