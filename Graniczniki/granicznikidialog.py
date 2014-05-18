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

        seg.setGeometry(QgsGeometry.fromPoint(point))
        pr.addFeatures([seg])

    def buttonClicked(self):
        plainText = self.textEdit.toPlainText()
        points = self.parsePoints(plainText)
        v_layer = QgsVectorLayer("POINT", "line", "memory")
        pr = v_layer.dataProvider()
        for point in points:
            self.addPointToLayer(pr, point)
        v_layer.updateExtents()
        QgsMapLayerRegistry.instance().addMapLayers([v_layer])