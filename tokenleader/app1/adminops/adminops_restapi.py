from flask import request, Blueprint, jsonify, current_app, make_response
from tokenleader.app1.adminops import admin_functions as af
from tokenleaderclient.configs.config_handler import Configs    
from  tokenleaderclient.client.client import Client 
from tokenleaderclient.rbac.enforcer import Enforcer
import json

adminops_bp = Blueprint('adminops_bp', __name__)
auth_config = Configs()
tlclient = Client(auth_config)
enforcer = Enforcer(tlclient)
 
@adminops_bp.route('/list/users', methods=['GET'])
@enforcer.enforce_access_rule_with_token('tokenleader.adminops.adminops_restapi.list_user')
def list_users(wfc):
    '''
    the function must have a mandatory wfc paramater for applying enforcer decorator
    '''   
    record = af.list_users()
    response_obj = {"status": record}
    return jsonify(response_obj)

@adminops_bp.route('/list/user/<username>', methods=['GET'])
def list_user_byname(username):
    #print('i got the name from http argument {}'.format(username))
    record = af.list_users(username)
    response_obj = {"status": record}
    return jsonify(response_obj)

@adminops_bp.route('/list/org', methods=['GET'])
@enforcer.enforce_access_rule_with_token('tokenleader.adminops.adminops_restapi.list_org')
def list_org(wfc):
    org_dict = af.list_org()
    obj_json = {"name": org_dict.get('name')}
    response_obj = {"status": obj_json}
    return jsonify(response_obj)

@adminops_bp.route('/list/dept', methods=['GET'])
@enforcer.enforce_access_rule_with_token('tokenleader.adminops.adminops_restapi.list_dept')
def list_dept(wfc):
    dept_dict = af.list_dept()
    obj_json = {"name": dept_dict.get('name')}
    response_obj = {"status": obj_json}
    return jsonify(response_obj)

@adminops_bp.route('/list/role', methods=['GET'])
@enforcer.enforce_access_rule_with_token('tokenleader.adminops.adminops_restapi.list_role')
def list_role(wfc):
    role_dict = af.list_role()
    obj_json = {"name": role_dict.get('name')}
    response_obj = {"status": obj_json}
    return jsonify(response_obj)

@adminops_bp.route('/list/ou', methods=['GET'])
@enforcer.enforce_access_rule_with_token('tokenleader.adminops.adminops_restapi.list_ou')
def list_ou(wfc):
    ou_dict = af.list_ou()
    obj_json = {"name": ou_dict.get('name')}
    response_obj = {"status": obj_json}
    return jsonify(response_obj)

@adminops_bp.route('/list/wfc', methods=['GET'])
@enforcer.enforce_access_rule_with_token('tokenleader.adminops.adminops_restapi.list_wfc')
def list_wfc():
    wfc_dict = af.list_wfc()
    obj_json = {"name": wfc_dict.get('name')}
    response_obj = {"status": obj_json}
    return jsonify(response_obj)


@adminops_bp.route('/add/user', methods=['POST'])
@enforcer.enforce_access_rule_with_token('tokenleader.adduser')
def add_user(wfc):
    data_must_contain = ['username', 'email', 'password', 'wfc', 'roles']
    for k in data_must_contain:
        if k not in request.json:
            return jsonify({"status": " the request must have the following \
            information {}".format(json.dumps(data_must_contain))})
    uname = request.json['username']
    email = request.json['email']
    pwd = request.json['password']
    wfc_name  = request.json['wfc']
    roles = request.json['roles']
    print('i got the name from http argument {}'.format(uname))
    record = af.register_user(uname, email, pwd, wfc_name, roles=roles)
    response_obj = {"status": record}
    return jsonify(response_obj)

@adminops_bp.route('/add/wfc', methods=['POST'])
def add_wfc():
    data_must_contain = ['fname', 'orgname', 'ou_name', 'dept_name']
    for f in data_must_contain:
        if f not in request.json:
            return {"status": " the request must have the following \
            information {}".data_must_contain}
    fname = request.json['fname']
    orgname = request.json['orgname']
    ou_name = request.json['ou_name']
    dept_name  = request.json['dept_name']
    record = af.register_work_func_context(fname, orgname, ou_name, dept_name)
    response_obj = {"status": record}
    return jsonify(response_obj)

# @adminops_bp.route('/add/ou/<ouname>', methods=['POST'])
# def add_orgunit_restapi(ouname):   
#     status = af.register_ou(ouname)
#     response_obj = {"status": status}
#     return jsonify(response_obj)

@adminops_bp.route('/add/ou', methods=['POST'])
def add_orgunit():
    data_must_contain = ['ouname']
    for k in data_must_contain:
        if k not in request.json:
            return jsonify({"status": " the request must have the following \
            information {}".format(json.dumps(data_must_contain))})
    ouname = request.json['ouname']
    print('i got the name from http argument {}'.format(ouname))
    record = af.register_ou(ouname)
    response_obj = {"status": record}
    return jsonify(response_obj)

@adminops_bp.route('/add/dept', methods=['POST'])
def add_dept():
    data_must_contain = ['deptname']
    for k in data_must_contain:
        if k not in request.json:
            return jsonify({"status": " the request must have the following \
            information {}".format(json.dumps(data_must_contain))})
    deptname = request.json['deptname']
    print('i got the name from http argument {}'.format(deptname))
    record = af.register_dept(deptname)
    response_obj = {"status": record}
    return jsonify(response_obj)


@adminops_bp.route('/add/org', methods=['POST'])
def add_org():
    data_must_contain = ['oname']
    for k in data_must_contain:
        if k not in request.json:
            return jsonify({"status": " the request must have the following \
            information {}".format(json.dumps(data_must_contain))})
    oname = request.json['oname']
    print('i got the name from http argument {}'.format(oname))
    record = af.register_org(oname)
    response_obj = {"status": record}
    return jsonify(response_obj)


@adminops_bp.route('/add/role', methods=['POST'])
def add_role():
    data_must_contain = ['rolename']
    for k in data_must_contain:
        if k not in request.json:
            return jsonify({"status": " the request must have the following \
            information {}".format(json.dumps(data_must_contain))})
    rolename = request.json['rolename']
    print('i got the name from http argument {}'.format(rolename))
    record = af.register_role(rolename)
    response_obj = {"status": record}
    return jsonify(response_obj)

@adminops_bp.route('/delete/user', methods=['POST'])
def delete_user(wfc):
    data_must_contain = ['uname']
    for k in data_must_contain:
        if k not in request.json:
            return jsonify({"status": " the request must have the following \
            information {}".format(json.dumps(data_must_contain))})
    uname = request.json['uname']
    print('i got the name from http argument {}'.format(uname))
    record = af.delete_user(uname)
    response_obj = {"status": record}
    return jsonify(response_obj)



@adminops_bp.route('/delete/user/<username>', methods=['DELETE'])
def delete_user_restapi(username):   
    status = af.delete_user(username)
    response_obj = {"status": status}
    return jsonify(response_obj)

@adminops_bp.route('/delete/ou/<ouname>', methods=['DELETE'])
def delete_ou_restapi(ouname):
    status = af.delete_ou(ouname)
    response_obj = {"status": status}
    return jsonify(response_obj)

@adminops_bp.route('/delete/org/<orgname>', methods=['DELETE'])
def delete_org_restapi(orgname):
    status = af.delete_org(orgname)
    response_obj = {"status": status}
    return jsonify(response_obj)

@adminops_bp.route('/delete/dept/<deptname>', methods=['DELETE'])
def delete_dept_restapi(deptname):
    status = af.delete_dept(deptname)
    response_obj = {"status": status}
    return jsonify(response_obj)

@adminops_bp.route('/delete/role/<rolename>', methods=['DELETE'])
def delete_role_restapi(rolename):
    status = af.delete_role(rolename)
    response_obj = {"status": status}
    return jsonify(response_obj)

@adminops_bp.route('/delete/wfc/<wfcname>', methods=['DELETE'])
def delete_wfc_restapi(wfcname):
    status = af.delete_wfc(wfcname)
    response_obj = {"status": status}
    return jsonify(response_obj)




