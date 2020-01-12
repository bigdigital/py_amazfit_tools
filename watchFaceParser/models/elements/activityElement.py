﻿import logging

from watchFaceParser.models.elements.basic.containerElement import ContainerElement


class ActivityElement(ContainerElement):
    def __init__(self, parameter, parent = None, name = None):
        self._kcalProgress = None
        self._pulseMeter = None
        self._steps = None
        self._distance = None
        self._pulse = None
        self._calories = None
        self._starImage = None
        self._circleRange = None
        super(ActivityElement, self).__init__(parameters = None, parameter = parameter, parent = parent, name = name)


    def getKcalProgress(self):
        return self._kcalProgress

    def getPulseMeter(self):
        return self._pulseMeter

    def getSteps(self):
        return self._steps


    def getDistance(self):
        return self._distance


    def getPulse(self):
        return self._pulse


    def getCalories(self):
        return self._calories


    def getStarImage(self):
        return self._starImage


    def getCircleRange(self):
        return self._circleRange


    def createChildForParameter(self, parameter):
        parameterId = parameter.getId()
        if parameterId == 1:
            from watchFaceParser.models.elements.activity.kcalProgressElement import KcalProgressElement
            self._kcalProgress = KcalProgressElement(parameter = parameter, parent = self, name = '?KcalProgress?')
            return self._kcalProgress
        #elif parameterId == 2:
        #    from watchFaceParser.models.elements.activity.caloriesElement import CaloriesElement
        #    self._calories = CaloriesElement(parameter = parameter, parent = self, name = '?Calories?')
        #    return self._calories
        elif parameterId == 3:
            from watchFaceParser.models.elements.activity.pulseElement import PulseElement
            self._pulse = PulseElement(parameter = parameter, parent = self, name = '?Pulse?')
            return self._pulse
        elif parameterId == 4:
            from watchFaceParser.models.elements.activity.distanceElement import DistanceElement
            self._distance = DistanceElement(parameter = parameter, parent = self, name = '?DistanceElement?')
            return self._distance
        elif parameterId == 5:
            from watchFaceParser.models.elements.activity.stepsElement import StepsElement
            self._steps = StepsElement(parameter = parameter, parent = self, name = '?Steps?')
            return self._steps
        elif parameterId == 7:
            from watchFaceParser.models.elements.activity.starImageElement import StarImageElement
            self._starImage = StarImageElement(parameter = parameter, parent = self, name = '?StarImage?')
            return self._starImage
        elif parameterId == 9:
            from watchFaceParser.models.elements.common.imageElement import ImageElement
            self._circleRange = ImageElement(parameter = parameter, parent = self, name = '?CircleRange?')
            return self._circleRange
        elif parameterId == 11:
            from watchFaceParser.models.elements.activity.pulseMeterElement import PulseMeterElement
            self._pulseMeter = PulseMeterElement(parameter = parameter, parent = self, name = '?PulseMeter?')
            return self._pulseMeter
        else:
            #print ("unsupported parameterid",parameterId)
            return super(ActivityElement, self).createChildForParameter(parameter)

