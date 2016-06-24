#!/usr/bin/env python
# -*- coding: : utf-8 -*-




##################################################
## DEPENDENCIES
import sys
import os
import os.path
try:
    import builtins as builtin
except ImportError:
    import __builtin__ as builtin
from os.path import getmtime, exists
import time
import types
from Cheetah.Version import MinCompatibleVersion as RequiredCheetahVersion
from Cheetah.Version import MinCompatibleVersionTuple as RequiredCheetahVersionTuple
from Cheetah.Template import Template
from Cheetah.DummyTransaction import *
from Cheetah.NameMapper import NotFound, valueForName, valueFromSearchList, valueFromFrameOrSearchList
from Cheetah.CacheRegion import CacheRegion
import Cheetah.Filters as Filters
import Cheetah.ErrorCatchers as ErrorCatchers
from LayerTemplateBase import LayerTemplateBase

##################################################
## MODULE CONSTANTS
VFFSL=valueFromFrameOrSearchList
VFSL=valueFromSearchList
VFN=valueForName
currentTime=time.time
__CHEETAH_version__ = '2.4.4'
__CHEETAH_versionTuple__ = (2, 4, 4, 'development', 0)
__CHEETAH_genTime__ = 1466685786.971
__CHEETAH_genTimestamp__ = 'Thu Jun 23 20:43:06 2016'
__CHEETAH_src__ = 'LayerTemplate.tmpl'
__CHEETAH_srcLastModified__ = 'Thu Jun 23 20:40:15 2016'
__CHEETAH_docstring__ = 'Autogenerated by Cheetah: The Python-Powered Template Engine'

if __CHEETAH_versionTuple__ < RequiredCheetahVersionTuple:
    raise AssertionError(
      'This template was compiled with Cheetah version'
      ' %s. Templates compiled before version %s must be recompiled.'%(
         __CHEETAH_version__, RequiredCheetahVersion))

##################################################
## CLASSES

class LayerTemplate(LayerTemplateBase):

    ##################################################
    ## CHEETAH GENERATED METHODS


    def __init__(self, *args, **KWs):

        super(LayerTemplate, self).__init__(*args, **KWs)
        if not self._CHEETAH__instanceInitialized:
            cheetahKWArgs = {}
            allowedKWs = 'searchList namespaces filter filtersLib errorCatcher'.split()
            for k,v in KWs.items():
                if k in allowedKWs: cheetahKWArgs[k] = v
            self._initCheetahInstance(**cheetahKWArgs)
        

    def writeBody(self, **KWS):



        ## CHEETAH: main method generated for this template
        trans = KWS.get("trans")
        if (not trans and not self._CHEETAH__isBuffering and not callable(self.transaction)):
            trans = self.transaction # is None unless self.awake() was called
        if not trans:
            trans = DummyTransaction()
            _dummyTrans = True
        else: _dummyTrans = False
        write = trans.response().write
        SL = self._CHEETAH__searchList
        _filter = self._CHEETAH__currentFilter
        
        ########################################
        ## START - generated method body
        
        #  首字母大写
        self._CHEETAH__globalSetVars["g_fullLayerName"] = '%s.%sLayer' % (VFFSL(SL,"namespace",True), VFFSL(SL,"name",True))
        self._CHEETAH__globalSetVars["g_guiFileName"] = 'res/UI/%s/Layer%s.json' % (VFFSL(SL,"namespace",True), VFFSL(SL,"name",True))
        #  首字母大写
        self._CHEETAH__globalSetVars["g_modelName"] = 'model.%sModel' % VFFSL(SL,"model",True)
        #  首字母大写
        self._CHEETAH__globalSetVars["g_globalEventName"] = 'common.NotifyType.%s_EVENT' % VFFSL(SL,"name",True)
        #  首字母大写
        self._CHEETAH__globalSetVars["g_globalEventFuncName"] = '__on%sEvent' % VFFSL(SL,"name",True)
        self._CHEETAH__globalSetVars["g_mediatorName"] = '%sLayerMediator' % VFFSL(SL,"name",True)
        self._CHEETAH__globalSetVars["g_fullMediatorName"] = '%s.$sLayerMediator' % (VFFSL(SL,"namespace",True), VFFSL(SL,"name",True))
        write(u'''//
// ''')
        _v = VFFSL(SL,"comment",True) # u'$comment' on line 12, col 4
        if _v is not None: write(_filter(_v, rawExpr=u'$comment')) # from line 12, col 4.
        write(u'''
//


/**
 * \u521d\u59cb\u5316\u3001\u6e05\u7406\uff0c\u4e0d\u8d1f\u8d23\u5176\u4ed6\u903b\u8f91
 *
 */
''')
        _v = VFFSL(SL,"g_fullLayerName",True) # u'$g_fullLayerName' on line 20, col 1
        if _v is not None: write(_filter(_v, rawExpr=u'$g_fullLayerName')) # from line 20, col 1.
        write(u'''\t\t\t\t\t\t\\= game.IView.extend({

\tUI_MAIN\t\t: ''')
        _v = VFFSL(SL,"g_guiFileName",True) # u'$g_guiFileName' on line 22, col 13
        if _v is not None: write(_filter(_v, rawExpr=u'$g_guiFileName')) # from line 22, col 13.
        write(u''',

\t__data\t\t: null,
\t__root\t\t: null,


\tctor:function(){
\t\tthis._super();

        //cc.log(''')
        _v = VFFSL(SL,"g_fullLayerName",True) # u'$g_fullLayerName' on line 31, col 18
        if _v is not None: write(_filter(_v, rawExpr=u'$g_fullLayerName')) # from line 31, col 18.
        write(u"""\\.DEBUG.format('ctor'));

\t\tthis.__data\t\t= game.Facade.getModelData(""")
        _v = VFFSL(SL,"g_modelName",True) # u'$g_modelName' on line 33, col 43
        if _v is not None: write(_filter(_v, rawExpr=u'$g_modelName')) # from line 33, col 43.
        write(u''');

\t\tthis.__root\t\t= ccs.load(this.UI_MAIN).node;
\t\tthis.addChild(this.__root);

        var comp        = null;

''')
        if VFFSL(SL,"btn_back",True) == True: # generated from line 40, col 1
            write(u"""        comp            = this.__root.getChildByName('btn_back');
        if(comp){
            comp.addTouchEventListener(this.__onTouchEvent, this);
        }
""")
        write(u'''
''')
        if VFFSL(SL,"btn_close",True) == True: # generated from line 47, col 1
            write(u"""        comp            = this.__root.getChildByName('btn_close');
        if(comp){
            comp.addTouchEventListener(this.__onTouchEvent, this);
        }
""")
        write(u'''
\t\tthis.__update();

\t\treturn true;
\t},


    destroy:function(){

    },


    __update:function(){

\t},


    __onTouchEvent:function(sender, type){
    \tswitch(type){
        case ccui.Widget.TOUCH_ENDED:
            switch(sender.name){
''')
        if VFFSL(SL,"btn_back",True) == True: # generated from line 74, col 1
            write(u"""            case 'btn_back':
                this.send(""")
            _v = VFFSL(SL,"g_globalEventName",True) # u'$g_globalEventName' on line 76, col 27
            if _v is not None: write(_filter(_v, rawExpr=u'$g_globalEventName')) # from line 76, col 27.
            write(u''', {
                    key             : sender.name
                });
                break;
''')
        write(u'''
''')
        if VFFSL(SL,"btn_close",True) == True: # generated from line 82, col 1
            write(u"""            case 'btn_close':
                this.send(""")
            _v = VFFSL(SL,"g_globalEventName",True) # u'$g_globalEventName' on line 84, col 27
            if _v is not None: write(_filter(_v, rawExpr=u'$g_globalEventName')) # from line 84, col 27.
            write(u''', {
                    key             : sender.name
                });
                break;
''')
        write(u'''
            default:
''')
        if VFFSL(SL,"global_event",True) == True: # generated from line 91, col 1
            write(u'''                this.send(''')
            _v = VFFSL(SL,"g_globalEventName",True) # u'$g_globalEventName' on line 92, col 27
            if _v is not None: write(_filter(_v, rawExpr=u'$g_globalEventName')) # from line 92, col 27.
            write(u''', {
                    key             : sender.name
                });
''')
        write(u'''                break;
            }
            break;
        }
    },

});

/********************************************************************/
/** static **/
/********************************************************************/

''')
        _v = VFFSL(SL,"g_fullLayerName",True) # u'$g_fullLayerName' on line 108, col 1
        if _v is not None: write(_filter(_v, rawExpr=u'$g_fullLayerName')) # from line 108, col 1.
        write(u"""\\.DEBUG\t\t\t\t\t\t\t= '""")
        #  $g_fullLayerName\.{0}: ';
        write(u'''

''')
        if VFFSL(SL,"mediator",True) == True: # generated from line 110, col 1
            write(u'''/********************************************************************/
/** mediator **/
/********************************************************************/

''')
            _v = VFFSL(SL,"g_fullMediatorName",True) # u'$g_fullMediatorName' on line 115, col 1
            if _v is not None: write(_filter(_v, rawExpr=u'$g_fullMediatorName')) # from line 115, col 1.
            write(u'''\t\t\t\t\t\t\t\\= game.LayerMediator.extend({


\tctor:function(view){
\t\tthis._super(view, true);

        //cc.log(''')
            _v = VFFSL(SL,"g_fullMediatorName",True) # u'$g_fullMediatorName' on line 121, col 18
            if _v is not None: write(_filter(_v, rawExpr=u'$g_fullMediatorName')) # from line 121, col 18.
            write(u"""\\.DEBUG.format('ctor'));
\t},


\tinit:function (){
\t\ttools.UIUtils.AutoClearManager.getInstance().addSubscribe('""")
            _v = VFFSL(SL,"g_mediatorName",True) # u'$g_mediatorName' on line 126, col 62
            if _v is not None: write(_filter(_v, rawExpr=u'$g_mediatorName')) # from line 126, col 62.
            write(u"""',
\t\t\tg_fullMediatorName, this.""")
            _v = VFFSL(SL,"g_globalEventFuncName",True) # u'$g_globalEventFuncName' on line 127, col 29
            if _v is not None: write(_filter(_v, rawExpr=u'$g_globalEventFuncName')) # from line 127, col 29.
            write(u""", this);
\t},


\tshow:function(parent){
\t\tthis._super(parent);
\t\tparent.addChild(this.currLayer);
\t},


\tfreshen:function(){

\t},


\tdestroy:function(){
\t\ttools.UIUtils.AutoClearManager.getInstance().removeAll('""")
            _v = VFFSL(SL,"g_mediatorName",True) # u'$g_mediatorName' on line 143, col 59
            if _v is not None: write(_filter(_v, rawExpr=u'$g_mediatorName')) # from line 143, col 59.
            write(u"""');
\t},


    """)
            _v = VFFSL(SL,"g_globalEventFuncName",True) # u'$g_globalEventFuncName' on line 147, col 5
            if _v is not None: write(_filter(_v, rawExpr=u'$g_globalEventFuncName')) # from line 147, col 5.
            write(u''':function(obj, unusedTarget){
        switch(obj.key){
''')
            if VFFSL(SL,"btn_back",True) == True: # generated from line 149, col 1
                write(u"""        case 'btn_back':
            this.popLayer(this);
            break;
""")
            write(u'''
''')
            if VFFSL(SL,"btn_close",True) == True: # generated from line 155, col 1
                write(u"""        case 'btn_close':
            this.popLayer(this, true);
            break;
""")
            write(u'''
        default:
            break;
        }
    },

});

/********************************************************************/
/** static **/
/********************************************************************/

''')
            _v = VFFSL(SL,"g_fullMediatorName",True) # u'$g_fullMediatorName' on line 172, col 1
            if _v is not None: write(_filter(_v, rawExpr=u'$g_fullMediatorName')) # from line 172, col 1.
            write(u"""\\.DEBUG\t\t\t\t\t\t\t= '""")
            #  $g_fullMediatorName\.{0}: ';
            write(u'''
''')
        
        ########################################
        ## END - generated method body
        
        return _dummyTrans and trans.response().getvalue() or ""
        
    ##################################################
    ## CHEETAH GENERATED ATTRIBUTES


    _CHEETAH__instanceInitialized = False

    _CHEETAH_version = __CHEETAH_version__

    _CHEETAH_versionTuple = __CHEETAH_versionTuple__

    _CHEETAH_genTime = __CHEETAH_genTime__

    _CHEETAH_genTimestamp = __CHEETAH_genTimestamp__

    _CHEETAH_src = __CHEETAH_src__

    _CHEETAH_srcLastModified = __CHEETAH_srcLastModified__

    _mainCheetahMethod_for_LayerTemplate= 'writeBody'

## END CLASS DEFINITION

if not hasattr(LayerTemplate, '_initCheetahAttributes'):
    templateAPIClass = getattr(LayerTemplate, '_CHEETAH_templateClass', Template)
    templateAPIClass._addCheetahPlumbingCodeToClass(LayerTemplate)


# CHEETAH was developed by Tavis Rudd and Mike Orr
# with code, advice and input from many other volunteers.
# For more information visit http://www.CheetahTemplate.org/

##################################################
## if run from command line:
if __name__ == '__main__':
    from Cheetah.TemplateCmdLineIface import CmdLineIface
    CmdLineIface(templateObj=LayerTemplate()).run()

