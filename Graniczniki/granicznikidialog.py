# -*- coding: utf-8 -*-
"""
/***************************************************************************
 GranicznikiDialog
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
"""

from PyQt4 import QtCore, QtGui
from ui_graniczniki import Ui_Graniczniki
from qgis.core import *
# create the dialog for zoom to point


class GranicznikiDialog(QtGui.QDialog, Ui_Graniczniki):
    def __init__(self):
        QtGui.QDialog.__init__(self)
        self.setupUi(self)
        self.loadButton.clicked.connect(self.buttonClicked)

    def buttonClicked(self):
        uri = QgsDataSourceURI()
        uri.setConnection("localhost", "5432", "wroclaw1", "postgres", "postgres")
        uri.setDataSource("public", "w_dzialki", "dzialki_geom")
        vlayer = QgsVectorLayer(uri.uri(), "layer_name_you_like", "postgres")
        iter = vlayer.getFeatures()
        text = ""
        self.textEdit.setText(text)
        caps = vlayer.dataProvider().capabilities()
        feat = QgsFeature()
        feat.setGeometry(QgsGeometry.fromRect(QgsRectangle(6419304,5663276, 6421448, 5664155)))
        (res, outFeats) = vlayer.dataProvider().addFeatures( [ feat ] )

