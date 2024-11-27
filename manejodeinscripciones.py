from aplicacion.modelos.usuario import Usuario
from aplicacion.repositorio.repositoriodeusuarios import RepositorioDeUsuarios

    #=================================
    #   Clase ManejoDe Inscripciones
    #   NO TIENE VARIABLES !!!
    #=================================
    class ManejoDeInscripciones:
        #=====================================================================
        #   Decorador staticmethod
        #   El objeto sólo tiene la función inscribirUsuario
        #   ENVUELVE LA FUNCIÓN SIN LLAMAR VARIABLES LOCALES
        #   el objeto ManejoDe Inscripciones es la interface intercambiable
        #=====================================================================
        @staticmethod
        def inscribirUsuario(usuario: Usuario, repositorioDeUsuarios: RepositorioDeUsuarios) -> None:
        print(" -----> Guardando usuario ... \n")
        repositorioDeUsuarios.abrir()
        repositorioDeUsuarios.guardar (usuario)
        repositorioDeUsuarios.cerrar()
