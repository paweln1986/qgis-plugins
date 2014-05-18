# -*- coding: utf-8 -*-
"""
/***************************************************************************
 Graniczniki
                                 A QGIS plugin
 Graniczniki
                             -------------------
        begin                : 2014-05-17
        copyright            : (C) 2014 by Pawel Nosal
        email                : p.nosal1986@gmail.com
 ***************************************************************************/

/***************************************************************************
 *                                                                         *
 *   This program is free software; you can redistribute it and/or modify  *
 *   it under the terms of the GNU General Public License as published by  *
 *   the Free Software Foundation; either version 2 of the License, or     *
 *   (at your option) any later version.                                   *
 *                                                                         *
 ***************************************************************************/
 This script initializes the plugin, making it known to QGIS.
"""

def classFactory(iface):
    # load Graniczniki class from file Graniczniki
    from graniczniki import Graniczniki
    return Graniczniki(iface)
