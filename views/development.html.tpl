<%
    from pprint import pformat
    import local_settings
    from controller.common import *

    rebase('skeleton.html.tpl', page=page)
%>

<div class="col-md-12">
    <div class="x_panel">
      <div class="x_content">
        <div class="row">
          <div class="col-sm-3 mail_list_column">
            % include('issue_form_new.html.tpl', page=page, only_button=False)

            % if page['result']['issues']:
              % for issue in page['result']['issues']['issues']:
                % include('issue_list_item.html.tpl', issue=issue)
              % end
            % end
          </div>
          <!-- /MAIL LIST -->

          <!-- CONTENT MAIL -->
          <div class="col-sm-9 mail_view">
            % if page['result'].has_key('current'):
              <div class="inbox-body">
                <div class="mail_heading row">
                    <div class="col-md-8">
                      % include('issue_form_reply.html.tpl', page=page, only_button=True)

                    </div>

                    <div class="col-md-4 text-right">
                      <p class="date">{{page['result']['current']['utc_created_on'].strftime('%y-%m-%d %H:%M')}}</p>
                    </div>

                    <div class="col-md-12">
                      <h4>{{page['result']['current']['title']}}</h4>
                    </div>
                </div>
                <div class="sender-info">
                    <div class="row">
                      <div class="col-md-12">
                        <span class="image">
                          <img src="{{page['result']['current']['reported_by']['avatar']}}" alt="[img]">
                        </span>&nbsp;
                        <strong>{{page['result']['current']['reported_by']['display_name']}}</strong>
                        <span class="badge">{{page['result']['current']['status']}}</span>
                        <span class="badge">{{page['result']['current']['metadata']['kind']}}</span>
                        <span class="badge">{{page['result']['current']['priority']}}</span>
                      </div>
                    </div>
                </div>
                <div class="view-mail">
                    {{!page['result']['current']['content']}}
                </div>
                % include('issue_reply_list.html.tpl', issue=page['result']['current'])
                % include('issue_attachment_list.html.tpl', issue=page['result']['current'])
                % include('issue_form_reply.html.tpl', page=page, only_button=False)
              </div>
            % end
          </div>
          <!-- /CONTENT MAIL -->
        </div>
      </div>
    </div>
</div>