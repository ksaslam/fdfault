from __future__ import division, print_function

from .domain import domain
from .output import output

class problem(object):
    """
    Class describing a dynamic rupture problem
    """
    def __init__(self,name):
        """
        Creates problem class with a given name, all other attributes set to zero
        """
        assert type(name) is str, "Problem name must be a string"

        self.name = name
        self.datadir = "data/"
        self.nt = 0
        self.dt = 0.
        self.ttot = 0.
        self.cfl = 0.
        self.ninfo = 10
        self.rkorder = 1
        self.d = domain()
        self.outputlist = []

    def get_name(self):
        "Returns problem name"
        return self.name

    def set_name(self, name):
        "Sets problem name"
        assert type(name) is str, "Problem name must be a string"
        self.name = name

    def set_datadir(self,datadir):
        "Sets problem data directory"
        assert type(datadir) is str, "Problem data directory must be a string"
        self.datadir = datadir

    def get_datadir(self):
        "Returns problem data directory"
        return self.datadir

    def set_nt(self,nt):
        "Sets number of time steps"
        assert nt >= 0, "Number of time steps cannot be less than zero"
        self.nt = int(nt)

    def get_nt(self):
        "Returns number of time steps"
        return self.nt

    def set_dt(self,dt):
        "Sets time step"
        assert dt >= 0., "Time step cannot be negative"
        self.dt = float(dt)

    def get_dt(self):
        "Returns time step"
        return self.dt

    def set_ttot(self,ttot):
        "Sets total integration time"
        assert ttot >= 0,"Integration time cannot be negative"
        self.ttot = float(ttot)
        
    def get_ttot(self):
        "Returns total integration time"
        return self.ttot

    def set_cfl(self,cfl):
        "Sets CFL ratio:"
        assert cfl >= 0. and cfl < 1., "CFL ratio must be between 0 and 1"
        self.cfl = float(cfl)

    def get_cfl(self):
        "Returns CFL ratio"
        return self.cfl

    def set_ninfo(self,ninfo):
        "Sets frequency of information output"
        assert ninfo > 0, "ninfo must be greater than zero"
        self.ninfo = int(ninfo)

    def get_ninfo(self):
        "Returns ninfo"
        return self.ninfo

    def set_rkorder(self,rkorder):
        "Sets order of RK method"
        assert rkorder == 1 or rkorder == 2 or rkorder == 3 or rkorder == 4, "RK order must be between 1 and 4"
        self.rkorder = int(rkorder)

    def get_rkorder(self):
        "Returns rkorder"
        return self.rkorder

    def get_sbporder(self):
        "Returns finite difference order"
        return self.d.get_sbporder()

    def set_sbporder(self,sbporder):
        "Sets finite difference order"
        self.d.set_sbporder(sbporder)

    def get_ndim(self):
        "Returns number of dimensions"
        return self.d.get_ndim()

    def set_ndim(self,ndim):
        "Sets number of dimensions"
        self.d.set_ndim(ndim)

    def get_mode(self):
        "Returns rupture mode"
        return self.d.get_mode()

    def set_mode(self, mode):
        "Sets rupture mode"
        self.d.set_mode(mode)

    def get_nx(self):
        "Returns number of spatial grid points"
        return self.d.get_nx()

    def get_nblocks_tot(self):
        "Returns total number of blocks"
        return self.d.get_nblocks_tot()

    def get_nblocks(self):
        "Returns number of blocks in each spatial dimension"
        return self.d.get_nblocks()

    def set_nblocks(self, nblocks):
        """
        Sets number of blocks
        Adds or deletes blocks from the list of blocks as needed
        """
        self.d.set_nblocks(nblocks)

    def get_nx_block(self):
        "Returns number of grid points in each block for each dimension (list of lists)"
        return self.d.get_nx_block()

    def set_nx_block(self,nx_block):
        """
        Set number of grid points in each block as a list of lists
        Input must be a list or tuple of length 3, with each item a list of integers representing
        the number of grid points for each block along the respective dimension
        For example, if nblocks = (3,2,1), then nblock[0] has length 3, nblock[1] has length 2,
        and nblock[2] has length 1
        """
        self.d.set_nx_block(nx_block)

    def get_block_lx(self,coords):
        "Returns size of block with coordinates coords"
        return self.d.get_block_lx(coords)

    def set_block_lx(self,coords,lx):
        "Sets block with coordinates coords to have dimension lx"
        self.d.set_block_lx(coords, lx)

    def get_block_xm(self,coords):
        "Returns location of block with coordinates coords"
        return self.d.get_block_xm(coords)

    def set_domain_xm(self,xm):
        "Sets lower left corner of domain to xm"
        self.d.set_domain_xm(xm)

    def get_mattype(self):
        "Returns material type"
        return self.d.get_mattype()

    def set_mattype(self, mattype):
        "Sets field and block material type"
        self.d.set_mattype(mattype)

    def set_material(self, newmaterial, coords = None):
        """
        Sets block material properties for given indices, if no coords provided does so for all blocks
        If setting all blocks, also changes material type in fields instance if necessary
        If setting a single block, material type must match that given in fields
        """
        self.d.set_material(newmaterial,coords)

    def get_bounds(self, coords, loc = None):
        """
        Returns boundary types, if location provided returns specific location, otherwise returns list
        locations correspond to the following: 0 = left, 1 = right, 2 = front, 3 = back, 4 = bottom, 5 = top
        Note that the location must be 0 <= loc < 2*ndim
        """
        return self.d.get_bounds(coords,loc)

    def set_bounds(self, coords, bounds, loc = None):
        """
        Sets boundary types
        Can either provide a list of strings specifying boundary type, or a single string and a location (integer)
        locations correspond to the following: 0 = left, 1 = right, 2 = front, 3 = back, 4 = bottom, 5 = top
        Note that the location must be 0 <= loc < 2*ndim
        """
        self.d.set_bounds(coords, bounds, loc)

    def get_block_surf(self, coords, loc):
        """
        Returns blockboundary surface for block with coords
        locations correspond to the following: 0 = left, 1 = right, 2 = front, 3 = back, 4 = bottom, 5 = top
        Note that the location must be 0 <= loc < 2*ndim
        """
        return self.d.get_block_surf(coords,loc)

    def set_block_surf(self, coords, loc, surf):
        """
        Sets boundary surface for block with coords
        locations correspond to the following: 0 = left, 1 = right, 2 = front, 3 = back, 4 = bottom, 5 = top
        Note that the location must be 0 <= loc < 2*ndim
        """
        self.d.set_block_surf(coords, loc, surf)

    def get_stress(self):
        "Returns intial stress values"
        return self.d.get_stress()

    def set_stress(self,s):
        "Sets uniform intial stress"
        self.d.set_stress(s)

    def get_nifaces(self):
        "Returns number of interfaces"
        return self.d.get_nifaces()

    def get_iftype(self, index = None):
        "Returns interface type of given index, if none provided returns full list"
        return self.d.get_iftype(index)

    def set_iftype(self, index, iftype):
        "Sets iftype of interface index"
        self.d.set_iftype(index, iftype)

    def get_iface_surf(self,index):
        "Returns interface surface for given index"
        return self.d.get_iface_surf(index)

    def set_iface_surf(self, index, surf):
        "Sets interface surface for given index"
        self.d.set_iface_surf(index,surf)

    def get_nloads(self, index):
        "Returns number of loads on given interface"
        return self.d.get_nloads(index)

    def add_load(self, newload, index = None):
        "Adds load to interface with index (either integer index or iterable)"
        self.d.add_load(newload, index)

    def get_direction(self, index):
        "Returns direction of interface index"
        return self.d.get_direction(index)

    def get_bm(self, index):
        "Returns block in minus direction of interface index"
        return self.d.get_bm(index)
        
    def get_bp(self, index):
        "Returns block in plus direction of interface index"
        return self.d.get_bp(index)

    def get_dc(self, index):
        "Returns slip weakening distance of interface index"
        return self.d.get_dc(index)

    def get_mus(self, index):
        "Returns static friction coefficient of interface index"
        return self.d.get_mus(index)

    def get_mud(self, index):
        "Returns dynamic friction coefficient of interface index"
        return self.d.get_mud(index)

    def get_params(self, index):
        "Returns friction parameters of interface index"
        return self.d.get_params(index)

    def set_dc(self, dc, index = None):
        "Sets slip weakening distance of interface index, if no index provided does so for all interfaces"
        self.d.set_dc(dc, index)

    def set_mus(self, mus, index = None):
        "Sets static friction coefficient of interface index, if no index provided does so for all interfaces"
        self.d.set_mus(mus, index)

    def set_mud(self, mud, index = None):
        "Sets dynamic friction coefficient of interface index, if no index provided does so for all interfaces"
        self.d.set_mud(mud, index)

    def set_params(self, dc, mus, mud, index = None):
        "Sets friction parameters of interface index, if no index provided does so for all interfaces"
        self.d.set_params(dc, mus, mud, index)

    def add_output(self, item):
        "Adds output item to output list"
        assert type(item) is output, "Item must be of type output"
        self.outputlist.append(item)

    def delete_output(self, index = None):
        "Deletes output item at given index (if none given, pops last item)"
        if index is None:
            self.outputlist.pop()
        else:
            assert index >= 0 and index < len(self.outputlist), "bad index"
            self.outputlist.pop(index)
    
    def write_input(self, filename = None, endian = '='):
        "Writes problem to input file"

        self.check()

        if (filename is None):
            f = open(self.name+".in",'w')
        else:
            f = open(filename+".in",'w')

        f.write("[fdfault.problem]\n")
        f.write(str(self.name)+"\n")
        f.write(str(self.datadir)+"\n")
        f.write(str(self.nt)+"\n")
        f.write(str(self.dt)+"\n")
        f.write(str(self.ttot)+"\n")
        f.write(str(self.cfl)+"\n")
        f.write(str(self.ninfo)+"\n")
        f.write(str(self.rkorder)+"\n")
        f.write("\n")
        self.d.write_input(f, self.name, endian)
        f.write("[fdfault.outputlist]\n")
        for item in self.outputlist:
            item.write_input(f)
        f.write("\n\n")
        f.close()

    def check(self):
        "Checks problem for errors"

        assert (self.ttot > 0. and self.nt > 0) or ((self.ttot > 0. or self.nt > 0) and (self.dt > 0. or self.cfl > 0.)), "Must specify two of nt, dt, ttot, or cfl (except dt and cfl)"

        for i in range(len(self.outputlist)):
            if self.outputlist[i].get_xp() > self.d.get_nx()[0]-1:
                print("xp greater than nx in output "+self.outputlist[i].get_name())
            if self.outputlist[i].get_yp() > self.d.get_nx()[1]-1:
                print("yp greater than ny in output "+self.outputlist[i].get_name())
            if self.outputlist[i].get_zp() > self.d.get_nx()[2]-1:
                print("zp greater than nz in output "+self.outputlist[i].get_name())
            if (self.nt > 0 and self.outputlist[i].get_tp() > self.nt-1):
                print("tp greater than nt in output "+self.outputlist[i].get_name())
            field = self.outputlist[i].get_field()
            
        self.d.check()
    
    def __str__(self):
        "Returns a string representation"
        outliststring = ""
        for item in self.outputlist:
            outliststring += "\n"+str(item)
        return ("Problem '"+self.name+"':\ndatadir = "+self.datadir+
                "\nnt = "+str(self.nt)+"\ndt = "+str(self.dt)+"\nttot = "+str(self.ttot)+"\ncfl = "+str(self.cfl)+
                "\nninfo = "+str(self.ninfo)+"\nrkorder = "+str(self.rkorder)+"\n\n"+str(self.d)+"\n\nOutput List:"+outliststring)