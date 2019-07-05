class EtcampyError(Exception):
    """etcampyで発生する例外の基底クラス"""
    pass

class CameraCannotOpenError(EtcampyError):
    """カメラが正常にオープンできない時に発生する例外"""
    pass