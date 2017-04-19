<!DOCTYPE html>
<html lang="en">
% include('html_head.html.tpl')

<body class="nav-md">
<div class="container body">
    <div class="main_container">
        % include('sidebar.html.tpl')

        % include('top_nav.html.tpl')

        <!-- page content -->
        <div class="right_col" role="main">
            <div class="">
                % include('page_title.html.tpl', title=page['title'], sub_title=page['sub_title'])

                <div class="clearfix"></div>

                <div class="row">
                    {{!base}}
                </div>
            </div>
        </div>
        <!-- /page content -->

        % include('page_footer.html.tpl')
    </div>
</div>

% include('javascript_includes.html.tpl', page_js=page['js'])

</body>
</html>