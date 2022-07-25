from yacs.config import CfgNode as CN


_C = CN()

_C.data = CN()
# train data pickle
_C.data.train_data       = ("./data/add_data_korean_coco_20220411_rollback.p", "train_data")
# test data pickle
_C.data.test_data        = ("./data/add_test_coco_ref_20220406_onlylen.p", "test_data")
# test image names pickle
_C.data.test_image_names = ("./data/add_test_filename_ref_20220406_onlylen.p", "test_image_names")

_C.save = CN()
# log dir name
_C.save.log_dir        = ("./logs/", "log_dir")
# checkpoint dir name
_C.save.checkpoint_dir = ("./checkpoint/", "checkpoint_dir")
# log and checkpoint name
_C.save.name           = ("debug", "log_name")

_C.model = CN()
# feature extractor model
_C.model.feature_extractor = ("efficientnet-b3", "feature_extractor")
# transformer components
_C.model.tf_type        = ("enc", "tf_type")
_C.model.encoder_layers = (1, "enc_layers")
_C.model.encoder_heads  = (1, "enc_heads")
_C.model.decoder_layers = (1, "dec_layers")
_C.model.decoder_heads  = (1, "dec_heads")

_C.param = CN()
# batch size
_C.param.batch_size      = (50, "batch_size")
# input spatial dim for transformer
_C.param.tf_input_dim    = (2, "tf_input_dim")
# whether combine word embedding to image feature or not
_C.param.tf_combine_word = (True, "combine_word")
# random masking ratio
_C.param.rand_mask       = (0.3, "rand_mask")
# gpu ids to use
_C.param.gpus            = ("0,1", "gpus")
# spatial size of extracted image feature
_C.param.ft_size         = (9, "ft_size")
# number of epochs
_C.param.num_epochs      = (50, "num_epochs")
# work embedding size
_C.param.embed_size      = (512, "embed_size")
# maximum word size
_C.param.max_words       = (40, "max_words")

# optimization settings
_C.param.optim = CN()
_C.param.optim.optimizer    = ("Adam", "optimizer")
_C.param.optim.momentum     = (0.9, "momentum")
_C.param.optim.lr           = (1e-3, "lr")
_C.param.optim.weight_decay = (1e-5, "weight_decay")
_C.param.optim.scheduler    = ("CosineAnnealingLR", "scheduler")


def get_cfg_defaults():
    return _C.clone()
