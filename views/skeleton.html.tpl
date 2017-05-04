<!DOCTYPE html>
<html lang="en">
% include('html_head.html.tpl')

<body class="nav-md">
<div class="container body">
    <div class="main_container">
        % include('sidebar.html.tpl', page=page)

        % include('top_nav.html.tpl', page=page)

        <!-- page content -->
        <div class="right_col" role="main">
            <div class="">
                % include('page_title.html.tpl', title=page['title'], sub_title=page['sub_title'])

                % if page['messages'] and len(page['messages']):
                    <div class="clearfix"></div>
                    <div class="x_content bs-example-popovers">
                        <div class="row">
                            % for msg in page['messages']:
                                <div
                                        class="alert alert-{{msg['type']}} {{'alert-dismissible' if msg['dismissible'] else ''}} fade in"
                                        role="alert"
                                >
                                    % if msg['dismissible']:
                                        <button class="close" type="button" data-dismiss="alert" aria-label="Close">
                                            <span aria-hidden="true">×</span>
                                        </button>
                                    % end
                                    {{!msg['content']}}
                                </div>
                            % end
                        </div>
                    </div>
                % end

                <div class="clearfix"></div>

                <div class="row">
                    {{!base}}
                </div>

                % if page['output'] and len(page['output']):
                    <div class="row">
                        <pre>
                            {{!page['output']}}
                        </pre>
                    </div>
                % end
            </div>
        </div>
        <!-- /page content -->

        % include('page_footer.html.tpl', page=page)
    </div>
</div>

% include('javascript_includes.html.tpl', page_js=page['js'])

</body>
</html>