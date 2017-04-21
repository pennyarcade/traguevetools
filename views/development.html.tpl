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
            % include('issue_form_new.html.tpl', page=page, only_button=False)

            % if result['issues']:
              % for issue in result['issues']['issues']:
                % include('issue_list_item.html.tpl', issue=issue)
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
                        % include('issue_form_reply.html.tpl', page=page, only_button=False)

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
                % include('issue_reply_list.html.tpl', issue=result['current'])
                % include('issue_attachment_list.html.tpl', issue=result['current'])
                <div class="btn-group">
                    % include('issue_form_reply.html.tpl', page=page, only_button=True)
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