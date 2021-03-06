from common import *
import configparser

#
# proposal i,x0,y0,x1,y1,score, label, (aux)
# roi      i,x0,y0,x1,y1
# box        x0,y0,x1,y1



class Configuration(object):

    def __init__(self):
        super(Configuration, self).__init__()
        self.version='configuration version \'xxx-kaggle\''

        #features
        self.scales = [2,  4,  8, 16]

        #
        # self.num_classes = 2 #include background class
        # self.border = 0.25
        #
        # #multi-rpn
        # self.rpn_base_sizes = [ 8, 16, 32, 64, ] #diameter
        # self.rpn_scales     = [ 2,  4,  8, 16  ]
        #
        # aspect = lambda s,x: (s*1/x**0.5,s*x**0.5)
        # self.rpn_base_apsect_ratios = [
        #     [(1,1) ],
        #     [(1,1), aspect(2**0.5,2), aspect(2**0.5,0.5),],
        #     [(1,1), aspect(2**0.5,2), aspect(2**0.5,0.5),],
        #     [(1,1), aspect(2**0.5,2), aspect(2**0.5,0.5),],
        # ]
        #
        #
        # self.rpn_train_bg_thresh_high = 0.5
        # self.rpn_train_fg_thresh_low  = 0.5
        #
        # self.rpn_train_nms_pre_score_threshold = 0.50
        # self.rpn_train_nms_overlap_threshold   = 0.85  #higher for more proposals for mask training
        # self.rpn_train_nms_min_size = 5
        #
        # self.rpn_test_nms_pre_score_threshold = 0.60
        # self.rpn_test_nms_overlap_threshold   = 0.75
        # self.rpn_test_nms_min_size = 5
        #
        #
        # #rcnn
        # self.rcnn_crop_size         = 14
        # self.rcnn_train_batch_size  = 32 #per image
        # self.rcnn_train_fg_fraction = 0.5
        # self.rcnn_train_fg_thresh_low  = 0.5
        # self.rcnn_train_bg_thresh_high = 0.5
        # self.rcnn_train_bg_thresh_low  = 0.0
        #
        # self.rcnn_train_min_size = 5
        # self.rcnn_train_nms_pre_score_threshold = 0.05
        # self.rcnn_train_nms_overlap_threshold   = 0.85  # high for more proposals for mask
        # self.rcnn_train_nms_min_size = 5
        #
        # self.rcnn_test_nms_pre_score_threshold = 0.50
        # self.rcnn_test_nms_overlap_threshold   = 0.85
        # self.rcnn_test_nms_min_size = 5
        #
        # #mask
        # self.mask_crop_size            = 14
        # self.mask_size                 = 28
        # self.mask_train_batch_size     = 32 #per image
        # self.mask_train_min_size       = 5
        # self.mask_train_fg_thresh_low  = self.rpn_train_fg_thresh_low
        #
        # self.mask_test_nms_pre_score_threshold = 0.1  #self.rpn_test_nms_pre_score_threshold
        # self.mask_test_nms_overlap_threshold = 0.20
        # self.mask_test_mask_threshold  = 0.5
        # self.mask_test_mask_min_area   = 8


    #-------------------------------------------------------------------------------------------------------
    def __repr__(self):
        d = self.__dict__.copy()
        str=''
        for k, v in d.items():
            str +=   '%32s = %s\n' % (k,v)

        return str


    def save(self, file):
        d = self.__dict__.copy()
        config = configparser.ConfigParser()
        config['all'] = d
        with open(file, 'w') as f:
            config.write(f)


    def load(self, file):
        # config = configparser.ConfigParser()
        # config.read(file)
        #
        # d = config['all']
        # self.num_classes     = eval(d['num_classes'])
        # self.multi_num_heads = eval(d['multi_num_heads'])
        raise NotImplementedError
