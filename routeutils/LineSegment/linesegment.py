from routeutils.Utils.utils import distanceMeteres, makeVector, angleBetweenVectors

class LineSegment:
    def __init__(self, pointA: tuple, pointB: tuple):
        self.pointA = pointA
        self.pointB = pointB
        
    def isPointInLine(self, point, distanceInMetersToBeInLine):
        distancePointToSegmentLine = self.__getDistancePointToLineSegment(point)
        
        if self.__isPointCloseToLineSegment(distancePointToSegmentLine, distanceInMetersToBeInLine):
            if self.__isPointOnLineLaterals(point):
                return True
        return False
    
    def __isPointCloseToLineSegment(self, distancePointToSegmentLine, distanceInMetersToBeInLine):
        return distancePointToSegmentLine <= distanceInMetersToBeInLine
    
    def __getDistancePointToLineSegment(self, point):
        closetsPointInLineSegment = self.__closestPointInLine(point)
        return distanceMeteres(point, closetsPointInLineSegment)
    
    def __isPointOnLineLaterals(self, point):
        vectorAP = makeVector(self.pointA, point)
        vectorAB = makeVector(self.pointA, self.pointB)
        
        vectorBP = makeVector(self.pointB, point)
        vectorBA = makeVector(self.pointB, self.pointA)
        
        angleAPAB = angleBetweenVectors(vectorAP, vectorAB)
        angleBPBA = angleBetweenVectors(vectorBP, vectorBA)
        return angleAPAB <= 90 and angleBPBA <= 90

    #https://stackoverflow.com/questions/3120357/get-closest-point-to-a-line
    def __closestPointInLine(self, point):
        a_to_p = [1,1]
        a_to_b = [1,1]

        a_to_p[0] = point[0] - self.pointA[0]
        a_to_p[1] = point[1] - self.pointA[1]
        a_to_b[0] = self.pointB[0] - self.pointA[0]
        a_to_b[1] = self.pointB[1] - self.pointA[1]

        atb2 = a_to_b[0] * a_to_b[0] + a_to_b[1] * a_to_b[1]
        atp_dot_atb = a_to_p[0] * a_to_b[0] + a_to_p[1] * a_to_b[1]
        
        t = 0
        if atb2 == 0:
            t = 1
        else:
            t = atp_dot_atb / atb2;

        if (t > 1): t = 1
        if (t < 0): t = 0

        return (self.pointA[0] + a_to_b[0] * t, self.pointA[1] + a_to_b[1] * t)