from routeutils import routeanalyser

def test_isPointInsideRoute_mustBeTrue():
    latitude = -30.033233564203634
    longitude = -51.21691256761551

    route = [
          [
            -51.22019290924072,
            -30.03246262969342
          ],
          [
            -51.21954381465912,
            -30.03261588823629
          ],
          [
            -51.21880352497101,
            -30.03279236747691
          ],
          [
            -51.21802568435669,
            -30.0329549138679
          ],
          [
            -51.217188835144036,
            -30.03315461335472
          ],
          [
            -51.216282248497,
            -30.033349668278966
          ],
          [
            -51.21572434902191,
            -30.033475060527536
          ]
        ]
        
    margin = 10

    assert routeanalyser.isPointInsideRoute(latitude=latitude, longitude=longitude, route=route, margin=margin) == True


def test_isPointInsideRoute_mustBeFalse():
    latitude = -30.033750226294742
    longitude = -51.21729478240013

    route = [
          [
            -51.22019290924072,
            -30.03246262969342
          ],
          [
            -51.21954381465912,
            -30.03261588823629
          ],
          [
            -51.21880352497101,
            -30.03279236747691
          ],
          [
            -51.21802568435669,
            -30.0329549138679
          ],
          [
            -51.217188835144036,
            -30.03315461335472
          ],
          [
            -51.216282248497,
            -30.033349668278966
          ],
          [
            -51.21572434902191,
            -30.033475060527536
          ]
        ]
        
    margin = 10

    assert routeanalyser.isPointInsideRoute(latitude=latitude, longitude=longitude, route=route, margin=margin) == False