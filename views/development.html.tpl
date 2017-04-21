<%
    from pprint import pformat

    page = {
        'title': 'Development',
        'sub_title': 'Bugs & Features',
        'js': '/static/js/development.js',
        'messages': messages,
        'output': output

    }

    rebase('skeleton.html.tpl', page=page)

%>

<div class="col-md-12">
    <div class="x_panel">
      <div class="x_content">
        <div class="row">
          <div class="col-sm-3 mail_list_column">
            <button id="compose" class="btn btn-sm btn-success btn-block" type="button">Create Issue</button>
            % if result['issues']:
              % for issue in result['issues']['issues']:
                <%
                    if issue['metadata']['kind'] == 'bug':
                        kclass = 'fa-bug'
                    elif issue['metadata']['kind'] == 'enhancement':
                        kclass = 'fa-lightbulb-o'
                    elif issue['metadata']['kind'] == 'proposal':
                        kclass = 'fa-comment'
                    elif issue['metadata']['kind'] == 'proposal':
                        kclass = 'fa-wrench'
                    else:
                        kclass = 'fa-square-o'
                    end

                    if issue['priority'] == 'trivial':
                        pclass = 'fa-smile-o'
                    elif issue['priority'] == 'minor':
                        pclass = 'fa-meh-o'
                    elif issue['priority'] == 'major':
                        pclass = 'fa-frown-o'
                    elif issue['priority'] == 'critical':
                        pclass = 'fa-exclamation'
                    elif issue['priority'] == 'blocker':
                        pclass = 'fa-bolt'
                    else:
                        pclass = 'fa-square-o'
                    end
                %>
                <a href="/development/{{issue['local_id']}}">
                  <div class="mail_list">
                    <div class="left">
                      % if issue['metadata']['kind']:
                        <i class="fa {{get('kclass')}}" title="{{issue['metadata']['kind']}}"></i>
                      % end
                      % if issue['priority']:
                        <i class="fa {{get('pclass')}}" title="{{issue['priority']}}"></i>
                      % end
                    </div>
                    <div class="right">
                      <h3>{{issue['reported_by']['display_name']}} <small>{{issue['created_on']}}</small></h3>
                      <p><span class="badge">{{issue['status']}}</span>&nbsp;{{issue['title']}}</p>
                    </div>
                  </div>
                </a>
              % end
            % end
          </div>
          <!-- /MAIL LIST -->

          <!-- CONTENT MAIL -->
          <div class="col-sm-9 mail_view">
            % if result.has_key('current'):
              <div class="inbox-body">
                <div class="mail_heading row">
                    <div class="col-md-8">
                      <div class="btn-group">
                        <button class="btn btn-sm btn-primary" type="button"><i class="fa fa-reply"></i> Reply</button>
                        <!--button class="btn btn-sm btn-default" type="button"  data-placement="top" data-toggle="tooltip" data-original-title="Forward"><i class="fa fa-share"></i></button>
                        <button class="btn btn-sm btn-default" type="button" data-placement="top" data-toggle="tooltip" data-original-title="Print"><i class="fa fa-print"></i></button>
                        <button class="btn btn-sm btn-default" type="button" data-placement="top" data-toggle="tooltip" data-original-title="Trash"><i class="fa fa-trash-o"></i></button-->
                      </div>
                    </div>

                    <div class="col-md-4 text-right">
                      <p class="date">{{result['current']['created_on']}}</p>
                    </div>

                    <div class="col-md-12">
                      <h4>{{result['current']['title']}}</h4>
                    </div>
                </div>
                <div class="sender-info">
                    <div class="row">
                      <div class="col-md-12">
                        <strong>Jon Doe</strong>
                        <span>(jon.doe@gmail.com)</span> to
                        <strong>me</strong>
                        <a class="sender-dropdown"><i class="fa fa-chevron-down"></i></a>
                      </div>
                    </div>
                  </div>
                <div class="view-mail">
                    {{!result['current']['content']}}
                </div>
                <ul class="list-unstyled msg_list">
                    % if result['current'].has_key('comments'):
                      % for comment in result['current']['comments']:
                        <li>
                          <a>
                            <span class="image">
                              <img src="{{comment['avatar']}}" alt="img">
                            </span>
                            <span>
                              <span>{{comment['display_name']}}</span>
                              <span class="time">{{comment['utc_created_on']}}</span>
                            </span>
                            <span class="message">{{comment['content']}}</span>
                          </a>
                        </li>
                      % end
                    % end
                  </ul>
                <div class="attachment">
                    <p>
                      <span><i class="fa fa-paperclip"></i> 3 attachments — </span>
                      <a href="#">Download all attachments</a> |
                      <a href="#">View all images</a>
                    </p>
                    <ul>
                      <li>
                        <a href="#" class="atch-thumb">
                          <img src="images/1.png" alt="img" />
                        </a>

                        <div class="file-name">
                          image-name.jpg
                        </div>
                        <span>12KB</span>


                        <div class="links">
                          <a href="#">View</a> -
                          <a href="#">Download</a>
                        </div>
                      </li>

                    </ul>
                  </div>
                <div class="btn-group">
                    <button class="btn btn-sm btn-primary" type="button"><i class="fa fa-reply"></i> Reply</button>
                    <!--button class="btn btn-sm btn-default" type="button"  data-placement="top" data-toggle="tooltip" data-original-title="Forward"><i class="fa fa-share"></i></button>
                    <button class="btn btn-sm btn-default" type="button" data-placement="top" data-toggle="tooltip" data-original-title="Print"><i class="fa fa-print"></i></button>
                    <button class="btn btn-sm btn-default" type="button" data-placement="top" data-toggle="tooltip" data-original-title="Trash"><i class="fa fa-trash-o"></i></button-->
                  </div>
              </div>
            % end
          </div>
          <!-- /CONTENT MAIL -->
        </div>
      </div>
    </div>
</div>