2019.04.15 —2019.09.03数据格式

| 编号 | 字段                | 数 据类型 | 含义                                                         |
| ---- | -------------------| --------- | ------------------------------------------------------------ |
| 1    | hostname           | string   | 服务机器                                                     |
| 2    | md5sha1             | string   | 查询文件标识，具体是md5还是md5+sha1,这个客户端决定。超大文件因为算md5时间太长，所以一般都不算，直接用全0，这种文件没有办法标   识，查杀都是靠其它特征，如路径特征等 |
| 3    | combo               | string   | 查询模块标识                                                 |
| 4    | full_path           | string   | 文件完整路径，urlencode                                      |
| 5    | is_x64              | int       | 是否是64位文件, -1：调用者未上传该信息， 0：不确定,   1：是  |
| 6    | level               | int       | 安全级别，(10:   纯白，20：白，30：未知级别，40：未查到md5，50：低疑似/外挂，60：高疑似，70：黑) |
| 7    | exist               | int       | 0不在db, 1在db,   kvdb是线上查询引擎，这个表示是否样本已存储 |
| 8    | flag                | int       | 文件标志                                                     |
| 9    | file_name           | string   | 文件名，urlencode                                            |
| 10   | has_desc            | int       | 是否有 file_desc 域                                          |
| 11   | mid                 | string   | 机器标识                                                     |
| 12   | product             | string   | 查询的产品名                                                 |
| 13   | upload              | int       | 是否要求客户端上传(0表示不上传，1表示上传)                   |
| 14   | is_sys_file         | int       | 是否系统文件                                                 |
| 15   | tv_sec              | int       | 查询时间戳                                                   |
| 16   | os_ver              | string   | 客户端上传文件对应的操作系统版本号                           |
| 17   | proto_ver          | string   | 云查询接口版本号，目前包括0，1，2   这个是通讯协议版本，目前最新版本为4 |
| 18   | compress_sign      | string   | 云查询流量是否启用压缩(0表示关闭，1表示开启) 已经弃用        |
| 19   | src                 | int       | 样本来源，自动(0)/人工(1)build标志                           |
| 20   | sub_level           | int       | 安全子类别                                                   |
| 21   | attribute _upload   | int       | 样本属性是否上传(0表示不上传，1表示上传)，未使用             |
| 22   | is_rep              | int       | 是否可替换(1表示可替换，0表示不可替换)，未使用               |
| 23   | malware _id         | string   | 恶意软件名称                                                 |
| 24   | class_id            | string   | 恶意软件类别                                                 |
| 25   | ext                 | string   | 业务扩展字段，查询引擎时，包上的ext信息，urlencode   , 这个字段的内容是客户端决定的，比如启动进程时可以包含一些启动进程的上下文信息， 下载可以包含一些下载地址之类的信息 |
| 26   | size                | int       | 文件大小，单位是字节bytes                                    |
| 27   | age                 | int       | 文件生命期，md5在系统中的年龄 单位：天                       |
| 28   | pop                 | int       | 文件流行度，这个字段也没用过，应该是个范围，比如0-1000，1000-5000，5000-10000，具体的范围不太清楚 |
| 29   | ps                  | string   | persistent，是否是只读数据，1是只读，0是非只读，暂未使用     |
| 30   | is_pe               | int       | 是否是PE文件，客户端上传                                     |
| 31   | client_ip           | string   | 客户端IP地址                                                 |
| 32   | storage_type       | int       | 存储类型，没有使用                                           |
| 33   | rowrule             | int       | 命中行规则（business_type=1）的规则id :   -1表示未命中，其他表示命中的规则号。 |
| 34   | rowrule_apply      | int       | 命中行规则之后的动作，-1未命中，0表示命中但未使用，1表示使用 |
| 35   | ori_level_sublevel | string   | 原始level.sublevel（未经修正），上面的level是经过规则加工的level，这个是原始的level。比如全0的样本原始level是40，但按照路径等特征，应   该判为70，上面的level就是70，这里的level就是40 |
| 36   | ext_hit             | string   | ext规则（business_type=2）命中情况，是否应用   : ext规则命中情况，是否应用，ext规则和行规则都是云规则的一种，应该是根据ext字段命中的 规则。 |
| 37   | row_ext             | string   | 上传报文行ext日志，urlencode   客户端上传的一些KV格式的信息，用于规则匹配，统计，去误报，查杀等，urlencode |
| 38   | is_win64            | int       | 是否为win64                                                  |
| 39   | locale              | string   | 本地化                                                       |
| 40   | encoding            | int       | 字符编码，gbk/utf8                                           |
| 41   | hit_white_cache    | int       | 是否命中了白名单cache : 1表示命中，0表示未命中               |
| 42   | rule_status        | string   | 规则命中状态 : 行规则，ext规则命中数量,ark，大规则   : 行规则如果设置了命中最大数量，此栏目显示当前命中了多少条，ext规则如果 设置了命中 最大数量，此栏目显示当前命中了多少条   （若为负数，表示-2表示命中并超限，-1表示没有设置命中限制） |
| 43   | row_bypass         | string   | 行规则（business_type=0，1，4，5，6）通路(bypass规则)   : 行规则通路情况(-1表示没有通路)，跟规则工具中行规则的状态相关 |
| 44   | ext_bypass         | string   | ext规则（business_type=2）通路（bypass规则）   : ext规则通路情况(-1表示没有通路)，跟规则工具中行规则的状态相关 |
| 45   | ark_log             | string   | 现在也没有打这个日志                                         |
| 46   | ie_ver              | string   | IE 版本号                                                    |
| 47   | uv                  | int       | user version   应用层逻辑版本信息,客户端服务端通讯协议版本，目前最新版本为4 |
| 48   | protocol            | string   | 通信协议: UDP或者HTTP                                        |
| 49   | mid_info            | string   | 命中后的mid信息,   格式为:mid_age:35\|\|mid_safe_age:4\|\|mid_tags:tag_id1,tag_id2,tag_id3 现在已经废弃 |
| 50   | product_ver        | string   | 客户端上传报文中的pver(version) Product   verison 调用该模块具体产品的版本，即cloudcom2.dll/cloudcom264.dll版本 |
| 51   | big_rule            | string   | 大规则（business_type=0）命中情况，是否应用   例如：-1.-1表示什么规则都没命中，123.0表示命中了123规则但没应用，123.1表示命中了123规 则并应用 |
| 52   | other_rules        | string   | 其他规则（business_type=4,5,6）命中状态   : 规则命中序号及命中状态，可以有多个(逗号分割)，例如 ",1123.123 ,2212.0,331.-1,332.-2"， 其中规   则key与状态码用.号分割，状态码含义：1表示命中并使用，0表示命中未使用，-1表示bypass规则，-2表示命中并超限 |
| 53   | engine_ext         | string   | 引擎md5原始extinfo 即：引擎里存的ext信息                     |
| 54   | uh                  | string   | uh   当客户端出现异常信息时，可以通过这个字段将信息带上来，比如取conf失败。字段格式如：u2h=2,noconf=0 是客户端的统计信息，u2h表示   udp失败转为http， noconf=1表示获取conf失败，使用lvsip请求 |
| 55   | consume             | string   | consume 客户端可以用来打点，目前该字段为空。   consume 客户端可以用来打点，上传客户端一些耗时统计 |
| 56   | consume_stage      | string   | 请求各阶段耗时和当前md5进行规则配置时的耗时，例如：ark=0.0,lines=5.4,package=5.5,big=5.3,line=0.0,sign=0.0,soft=0.0（当前没打信息） |
| 57   | is_req_utf8        | string   | 请求是否采用utf8编码                                         |
| 58   | hit_querykey       | int       | 是否包含通过规则或客户端上行的querykey查到的数据,1包含，0不包含 |
| 59   | region              | string   | 用户的地域信息：country_name,province_name,city_name,zip_code,phone_area_code,isp,city_level,large_region_code,province_code |
| 60   | rule_hitinfo       | string   | 重要命中的所有规则KEY和状态(所有bussinesstype的规则日志)，将之前的epe_num,   fpe_num, spe_num及状态合并到该列 |
| 61   | m2                  | string   | 新的mid算法计算的44位mid                                     |
| 62   | pid                 | string   | 客户端渠道号                                                 |
| 63   | sha256              | string   | 文件的标识sha256                                             |
| 64   | 数据来源            |           |                                                              |

YcsAdData数据格式

| 编号 | 字段名称 | 字段类型及长度 | 字段业务含义            |
| ---- | -------- | -------------- | ----------------------- |
| 1    | rowkey   | String         | 所有字段按\t拼接后取MD5 |
| 2    | Md5      | String         | 样本md5                 |
| 3    | Path     | String         | 样本路径                |
| 4    | Level    | Int            | 样本安全级别            |
| 5    | Mid      | String         | 客户端唯一标识          |
| 6    | time     | Long           | 时间                    |
| 7    | ClinetIp | String         | 客户端ip                |
| 8    | HiDst    | String         | 目标进程路径            |
| 9    | HiSrc    | String         | 来源进程路径            |
| 10   | HiScl    | String         | 来源进程启动命令行      |
| 11   | HiCle    | String         | 目标进程启动命令行      |
| 12   | HiItn    | String         | 内部名称                |
| 13   | HiOrn    | String         | 原始文件名              |
| 14   | HiDurl   | String         | 下载链接                |
| 15   | HiPurl   | String         | 父页面链接              |
| 16   | HiUzp    | String         | 进程链来源标识          |
| 17   | HiDlt    | String         | 进程连下载来源标识      |
| 18   | HiLnk    | String         | 启动进程的快捷方式路径  |
| 19   | HiMD5PAR | String         | 来源进程md5             |

skyeye_nd_data格式说明

| 编号 | 字段名称  | 字段类型及长度 | 字段业务含义            |
| ---- | --------- | -------------- | ----------------------- |
| 1    | rowkey    | String         | 所有字段按\t拼接后取MD5 |
| 2    | ndtype    | Int            | ID                      |
| 3    | md5       | String         | 样本md5                 |
| 4    | filelevel | Int            | 样本安全级别            |
| 5    | mid       | String         | 客户端唯一标识          |
| 6    | clientip  | String         | 客户端ip                |
| 7    | time      | Long           | 时间                    |
| 8    | dstip     | String         | 对端IP                  |
| 9    | host      | String         | HTTP Host               |
| 10   | url       | String         | HTTP URL                |
| 11   | filepath  | String         | 文件路径                |
| 12   | rp        | Int            | 对端端口                |

skyeye_multi_analyze_download数据格式

| 编号 | 字段名称        | 字段类型及长度 | 字段业务含义   |
| ---- | --------------- | -------------- | -------------- |
| 1    | md5             | String         | 样本md5        |
| 2    | sha1            | String         | sha1           |
| 3    | file_name       | String         | 文件名         |
| 4    | level           | Int            | 样本安全级别   |
| 5    | mid             | String         | 客户端唯一标识 |
| 6    | ip              | String         | 客户端ip       |
| 7    | download_domain | String         | 下载域名       |
| 8    | parent_domain   | String         | 父域名         |
| 9    | file_path       | String         | 文件完整路径   |
| 10   | parent_url      | String         | 父页面链接     |
| 11   | download_url    | String         | 下载链接       |
| 12   | file_size       | Long           | 文件大小       |
| 13   | fda             | String         | 文件DNA 串     |
| 14   | fbs             | Long           | 文件DNA Size   |
| 15   | file_list       | String         | 文件列表       |
| 16   | parent_fullpath | String         | 父路径         |
| 17   | time            | Long           | 时间           |