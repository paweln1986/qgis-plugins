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
        self.saveButton.clicked.connect(self.savePoints)

    def parsePoints(self, plainText):
        points = []
        splittedText = plainText.split("\n")
        for s in splittedText:
            p = s.split()
            qgis_point = QgsPoint(float(p[2]), float(p[1]))
            points.append(qgis_point)
        return points


    def addPointToLayer(self, pr, point):
        seg = QgsFeature()
        seg.initAttributes(4);
        seg.setAttribute(0, "nextval('w_d202_202022_tekst_id_seq'::regclass)")
        seg.setAttribute(1, 1959)
        seg.setAttribute(2, 0)
        seg.setAttribute(3, 14173631)
        seg.setGeometry(QgsGeometry.fromPoint(point))
        pr.addFeatures([seg])


    def prepareLayerInMemory(self, points):
        self.v_layer = QgsVectorLayer("POINT", "line", "memory")
        pr = self.v_layer.dataProvider()
        for point in points:
            self.addPointToLayer(pr, point)
        self.v_layer.updateExtents()
        QgsMapLayerRegistry.instance().addMapLayers([self.v_layer])

    def savePoints(self):
        uri = QgsDataSourceURI()
        uri.setConnection("localhost", "5432", "wroclaw1", "postgres", "postgres")
        uri.setDataSource("public", "w_d202_202022_tekst", "d202_202022_tekst_geom")
        vlayer = QgsVectorLayer(uri.uri(), "layer_name_you_like", "postgres")
        pr = vlayer.dataProvider()
        vlayer.startEditing()
        for point in self.points:
            self.addPointToLayer(pr, point)
        vlayer.updateExtents()
        QgsMapLayerRegistry.instance().addMapLayers([vlayer])
        QgsMapLayerRegistry.instance().removeMapLayer(self.v_layer.id())

    def buttonClicked(self):
        plainText = self.textEdit.toPlainText()
        self.points = self.parsePoints(plainText)
        self.prepareLayerInMemory(self.points)
        self.saveButton.setEnabled(True)