<!-- jQuery -->
<script src="/static/node_modules/gentelella/vendors/jquery/dist/jquery.min.js"></script>
<!-- Bootstrap -->
<script src="/static/node_modules/gentelella/vendors/bootstrap/dist/js/bootstrap.min.js"></script>
<!-- FastClick -->
<script src="/static/node_modules/gentelella/vendors/fastclick/lib/fastclick.js"></script>

<!-- Custom Page Scripts -->
% if defined('page_js'):
    % for item in page_js:
        <script src="{{item}}"></script>
    % end
% end

<!-- Custom Theme Scripts -->
<script src="/static/node_modules/gentelella/build/js/custom.min.js"></script>
