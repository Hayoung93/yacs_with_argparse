import argparse
from yacs.config import CfgNode
from configs.train_config import get_cfg_defaults


def get_args():
    parser = argparse.ArgumentParser(description='See configs/train_config.py for detailed information')
    
    parser.add_argument("--train_data", type=str)
    parser.add_argument("--test_data", type=str)
    parser.add_argument("--test_image_names", type=str)
    parser.add_argument("--log_dir", type=str)
    parser.add_argument("--gpus", type=str, default="0,1,2,3")

    args = parser.parse_args()
    cfg = get_cfg_defaults()
    cfg = merge_args(args, cfg)
    return cfg


def merge_args(args, cfg):
    new_cfg = CfgNode({})
    new_cfg.set_new_allowed(True)
    key_gen = get_cfg_keys(cfg, cfg.keys())
    while True:
        try:
            key = next(key_gen)
            value, args_key = eval("cfg." + key)
            if (args_key in args) and (eval("args." + args_key) is not None):
                value = eval("args." + args_key)
            key_split =  key.split(".")
            t1 = {key_split[-1]: value}
            t2 = {}
            for k in key_split[:-1][::-1]:
                if t1 == {}:
                    t1[k] = t2
                    t2 = {}
                else:
                    t2[k] = t1
                    t1 = {}
            if t1 == {}:
                t2 = CfgNode(t2)
                new_cfg = merge_cfg(t2, new_cfg)
            else:
                t1 = CfgNode(t1)
                new_cfg = merge_cfg(t1, new_cfg)
        except StopIteration:
            break
    return new_cfg


def get_cfg_keys(cn, keys):
    for key in keys:
        cur_node = eval("cn." + key)
        if type(cur_node) == CfgNode:
            yield from get_cfg_keys(cn, list(map(lambda x: key + "." + x, cur_node.keys())))
        else:
            yield key

def merge_cfg(a, b):
    for k, v in a.items():
        if k in b:
            if isinstance(v, CfgNode):
                merge_cfg(v, b[k])
            else:
                b[k] = v
        else:
            b[k] = v
    return b

