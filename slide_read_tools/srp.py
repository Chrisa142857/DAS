
# from libs.sdpc.sdpc import Sdpc
from slide_read_tools.libs.srp.pysrp import Srp


class SrpProxy:

    def __init__(self):
        self._ors = Srp()

    def open(self, slide_path):
        '''
        :param slide_path:
        :return, :
        '''
        self._ors.open(slide_path)
        self._proporties = self._ors.getAttrs()
        print(self._proporties)

    def mpp(self): return self._mppx()
    def _mppx(self): return self._proporties['mpp']
    def _mppy(self): return self._proporties['mpp']
    def boundsx(self): return 0
    def boundsy(self): return 0
    def width(self): return self._proporties['width']
    def height(self): return self._proporties['height']

    def close(self):
        if self._ors is not None:
            self._ors.close()


srr = SrpProxy()