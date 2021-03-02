﻿"""
 * Copyright 2020, Departamento de sistemas y Computación,
 * Universidad de Los Andes
 *
 *
 * Desarrolado para el curso ISIS1225 - Estructuras de Datos y Algoritmos
 *
 *
 * This program is free software: you can redistribute it and/or modify
 * it under the terms of the GNU General Public License as published by
 * the Free Software Foundation, either version 3 of the License, or
 * (at your option) any later version.
 *
 * This program is distributed in the hope that it will be useful,
 * but WITHOUT ANY WARRANTY; without even the implied warranty of
 * MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
 * GNU General Public License for more details.
 *
 * You should have received a copy of the GNU General Public License
 * along withthis program.  If not, see <http://www.gnu.org/licenses/>.
 *
 * Contribuciones:
 *
 * Dario Correal - Version inicial
 """


import config as cf
from DISClib.ADT import list as lt
from DISClib.Algorithms.Sorting import shellsort as sa
assert cf

"""
Se define la estructura de un catálogo de videos. El catálogo tendrá dos listas, una para los videos, otra para las categorias de
los mismos.
"""
#---------------------------------------------------------------------------------------------------------------------------------------
# Construccion de modelos
#---------------------------------------------------------------------------------------------------------------------------------------


def newCatalog(type):
    """
    Inicializa el catalogo de videos, crea una lista vacia para guardar:
    - Todos los videos
    - Las Categorias de los videos
    """
    catalog = {'videos': None,
               'categories': None}

    catalog['videos'] = lt.newList(type)
    catalog['categories'] = lt.newList(type)

    return catalog


#---------------------------------------------------------------------------------------------------------------------------------------
# Funciones para agregar informacion al catalogo
#---------------------------------------------------------------------------------------------------------------------------------------


def addVideoInfo(catalog, line):
    #Se adiciona la line del video a la lista de videos
    lt.addLast(catalog['videos'],line)
    
def addCategory(catalog, line):
    #Se adiciona la line del video a la lista de videos
    lt.addLast(catalog['categories'],line)
    
#---------------------------------------------------------------------------------------------------------------------------------------
# Funciones para creacion de datos
#---------------------------------------------------------------------------------------------------------------------------------------


#---------------------------------------------------------------------------------------------------------------------------------------
# Funciones de consulta
#---------------------------------------------------------------------------------------------------------------------------------------

def getTopViews(catalog, number_of_videos):
    """ 
    Retorna los videos más vistos
    """
    videos = catalog['videos']
    topViews = lt.newList()
    for position in range(1, number_of_videos+1):
        video = lt.getElement(videos, position)
        lt.addLast(topViews, video)
    return topViews

#---------------------------------------------------------------------------------------------------------------------------------------
# Funciones utilizadas para comparar elementos dentro de una lista
#---------------------------------------------------------------------------------------------------------------------------------------


def cmpVideosByViews(video_1,video_2):
    return (int(video_1['views'])>int(video_2['views']))

    
#---------------------------------------------------------------------------------------------------------------------------------------
# Funciones de ordenamiento
#---------------------------------------------------------------------------------------------------------------------------------------