# Import flask dependencies
from flask import Blueprint, request, jsonify
import re

mod_auth = Blueprint('auth', __name__, url_prefix='/auth')


@mod_auth.route('/signin', methods=['GET'])
def signin():

    filters_url = "pdf:true;peerRevd:true;lx:500-800,750-1200;subj:american%20history "
    matches = re.compile("(?<!\\\\);").split(filters_url)


    return jsonify(matches)

