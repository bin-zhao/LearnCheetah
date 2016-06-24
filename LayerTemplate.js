//
// 洗炼
//


/**
 * 初始化、清理，不负责其他逻辑
 *
 */
role.RoleFlushLayer						\= game.IView.extend({

	UI_MAIN		: res/UI/role/LayerRoleFlush.json,

	__data		: null,
	__root		: null,


	ctor:function(){
		this._super();

        //cc.log(role.RoleFlushLayer\.DEBUG.format('ctor'));

		this.__data		= game.Facade.getModelData(model.RoleModel);

		this.__root		= ccs.load(this.UI_MAIN).node;
		this.addChild(this.__root);

        var comp        = null;

        comp            = this.__root.getChildByName('btn_back');
        if(comp){
            comp.addTouchEventListener(this.__onTouchEvent, this);
        }

        comp            = this.__root.getChildByName('btn_close');
        if(comp){
            comp.addTouchEventListener(this.__onTouchEvent, this);
        }

		this.__update();

		return true;
	},


    destroy:function(){

    },


    __update:function(){

	},


    __onTouchEvent:function(sender, type){
    	switch(type){
        case ccui.Widget.TOUCH_ENDED:
            switch(sender.name){
            case 'btn_back':
                this.send(common.NotifyType.RoleFlush_EVENT, {
                    key             : sender.name
                });
                break;

            case 'btn_close':
                this.send(common.NotifyType.RoleFlush_EVENT, {
                    key             : sender.name
                });
                break;

            default:
                this.send(common.NotifyType.RoleFlush_EVENT, {
                    key             : sender.name
                });
                break;
            }
            break;
        }
    },

});

/********************************************************************/
/** static **/
/********************************************************************/

role.RoleFlushLayer\.DEBUG							= '

/********************************************************************/
/** mediator **/
/********************************************************************/

role.RoleFlushLayerMediator							\= game.LayerMediator.extend({


	ctor:function(view){
		this._super(view, true);

        //cc.log(role.RoleFlushLayerMediator\.DEBUG.format('ctor'));
	},


	init:function (){
		tools.UIUtils.AutoClearManager.getInstance().addSubscribe('RoleFlushLayerMediator',
			g_fullMediatorName, this.__onRoleFlushEvent, this);
	},


	show:function(parent){
		this._super(parent);
		parent.addChild(this.currLayer);
	},


	freshen:function(){

	},


	destroy:function(){
		tools.UIUtils.AutoClearManager.getInstance().removeAll('RoleFlushLayerMediator');
	},


    __onRoleFlushEvent:function(obj, unusedTarget){
        switch(obj.key){
        case 'btn_back':
            this.popLayer(this);
            break;

        case 'btn_close':
            this.popLayer(this, true);
            break;

        default:
            break;
        }
    },

});

/********************************************************************/
/** static **/
/********************************************************************/

role.RoleFlushLayerMediator\.DEBUG							= '
