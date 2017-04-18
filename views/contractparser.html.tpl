<!DOCTYPE html>
<html lang="en">
<head>
    <meta http-equiv="Content-Type" content="text/html; charset=UTF-8">
    <!-- Meta, title, CSS, favicons, etc. -->
    <meta charset="utf-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1">

    <title>New Eden Trade Guild Tool Box</title>

    <!-- Bootstrap -->
    <link href="/static/node_modules/gentelella/vendors/bootstrap/dist/css/bootstrap.min.css" rel="stylesheet">
    <!-- Font Awesome -->
    <link href="/static/node_modules/gentelella/vendors/font-awesome/css/font-awesome.min.css" rel="stylesheet">
    <!-- iCheck -->
    <link href="/static/node_modules/gentelella/vendors/iCheck/skins/flat/green.css" rel="stylesheet">
    <!-- Datatables -->
    <link href="/static/node_modules/gentelella/vendors/datatables.net-bs/css/dataTables.bootstrap.min.css"
          rel="stylesheet">
    <link href="/static/node_modules/gentelella/vendors/datatables.net-buttons-bs/css/buttons.bootstrap.min.css"
          rel="stylesheet">
    <link href="/static/node_modules/gentelella/vendors/datatables.net-fixedheader-bs/css/fixedHeader.bootstrap.min.css"
          rel="stylesheet">
    <link href="/static/node_modules/gentelella/vendors/datatables.net-responsive-bs/css/responsive.bootstrap.min.css"
          rel="stylesheet">
    <link href="/static/node_modules/gentelella/vendors/datatables.net-scroller-bs/css/scroller.bootstrap.min.css"
          rel="stylesheet">

    <!-- Custom Theme Style -->
    <link href="/static/node_modules/gentelella/build/css/custom.min.css" rel="stylesheet">
</head>

<body class="nav-md">
<div class="container body">
    <div class="main_container">
        <div class="col-md-3 left_col">
            <div class="left_col scroll-view">
                <div class="navbar nav_title" style="border: 0;">
                    <a href="index.html" class="site_title"><i class="fa fa-bar-chart"></i> <span>TRAGU Tools</span></a>
                </div>

                <div class="clearfix"></div>

                <!-- menu profile quick info -->
                <!-- div class="profile">
                  <div class="profile_pic">
                    <img src="images/img.jpg" alt="..." class="img-circle profile_img">
                  </div>
                  <div class="profile_info">
                    <span>Welcome,</span>
                    <h2>John Doe</h2>
                  </div>
                </div -->
                <!-- /menu profile quick info -->

                <br/>

                <!-- sidebar menu -->
                <div id="sidebar-menu" class="main_menu_side hidden-print main_menu">
                    <div class="menu_section">
                        <h3>General</h3>
                        <ul class="nav side-menu">
                            <li><a><i class="fa fa-home"></i> Home <span class="fa fa-chevron-down"></span></a>
                                <!--ul class="nav child_menu">
                                  <li><a href="index.html">Dashboard</a></li>
                                  <li><a href="index2.html">Dashboard2</a></li>
                                  <li><a href="index3.html">Dashboard3</a></li>
                                </ul-->
                            </li>
                            <!-- li><a><i class="fa fa-edit"></i> Forms <span class="fa fa-chevron-down"></span></a>
                              <ul class="nav child_menu">
                                <li><a href="form.html">General Form</a></li>
                                <li><a href="form_advanced.html">Advanced Components</a></li>
                                <li><a href="form_validation.html">Form Validation</a></li>
                                <li><a href="form_wizards.html">Form Wizard</a></li>
                                <li><a href="form_upload.html">Form Upload</a></li>
                                <li><a href="form_buttons.html">Form Buttons</a></li>
                              </ul>
                            </li -->
                            <!-- li><a><i class="fa fa-desktop"></i> UI Elements <span class="fa fa-chevron-down"></span></a>
                              <ul class="nav child_menu">
                                <li><a href="general_elements.html">General Elements</a></li>
                                <li><a href="media_gallery.html">Media Gallery</a></li>
                                <li><a href="typography.html">Typography</a></li>
                                <li><a href="icons.html">Icons</a></li>
                                <li><a href="glyphicons.html">Glyphicons</a></li>
                                <li><a href="widgets.html">Widgets</a></li>
                                <li><a href="invoice.html">Invoice</a></li>
                                <li><a href="inbox.html">Inbox</a></li>
                                <li><a href="calendar.html">Calendar</a></li>
                              </ul>
                            </li-->
                            <!--li><a><i class="fa fa-table"></i> Tables <span class="fa fa-chevron-down"></span></a>
                              <ul class="nav child_menu">
                                <li><a href="tables.html">Tables</a></li>
                                <li><a href="tables_dynamic.html">Table Dynamic</a></li>
                              </ul>
                            </li-->
                            <!--li><a><i class="fa fa-bar-chart-o"></i> Data Presentation <span class="fa fa-chevron-down"></span></a>
                              <ul class="nav child_menu">
                                <li><a href="chartjs.html">Chart JS</a></li>
                                <li><a href="chartjs2.html">Chart JS2</a></li>
                                <li><a href="morisjs.html">Moris JS</a></li>
                                <li><a href="echarts.html">ECharts</a></li>
                                <li><a href="other_charts.html">Other Charts</a></li>
                              </ul>
                            </li-->
                            <!--li><a><i class="fa fa-clone"></i>Layouts <span class="fa fa-chevron-down"></span></a>
                              <ul class="nav child_menu">
                                <li><a href="fixed_sidebar.html">Fixed Sidebar</a></li>
                                <li><a href="fixed_footer.html">Fixed Footer</a></li>
                              </ul>
                            </li-->
                        </ul>
                    </div>
                    <!--div class="menu_section">
                      <h3>Live On</h3>
                      <ul class="nav side-menu">
                        <li><a><i class="fa fa-bug"></i> Additional Pages <span class="fa fa-chevron-down"></span></a>
                          <ul class="nav child_menu">
                            <li><a href="e_commerce.html">E-commerce</a></li>
                            <li><a href="projects.html">Projects</a></li>
                            <li><a href="project_detail.html">Project Detail</a></li>
                            <li><a href="contacts.html">Contacts</a></li>
                            <li><a href="profile.html">Profile</a></li>
                          </ul>
                        </li>
                        <li><a><i class="fa fa-windows"></i> Extras <span class="fa fa-chevron-down"></span></a>
                          <ul class="nav child_menu">
                            <li><a href="page_403.html">403 Error</a></li>
                            <li><a href="page_404.html">404 Error</a></li>
                            <li><a href="page_500.html">500 Error</a></li>
                            <li><a href="plain_page.html">Plain Page</a></li>
                            <li><a href="login.html">Login Page</a></li>
                            <li><a href="pricing_tables.html">Pricing Tables</a></li>
                          </ul>
                        </li>
                        <li><a><i class="fa fa-sitemap"></i> Multilevel Menu <span class="fa fa-chevron-down"></span></a>
                          <ul class="nav child_menu">
                              <li><a href="#level1_1">Level One</a>
                              <li><a>Level One<span class="fa fa-chevron-down"></span></a>
                                <ul class="nav child_menu">
                                  <li class="sub_menu"><a href="level2.html">Level Two</a>
                                  </li>
                                  <li><a href="#level2_1">Level Two</a>
                                  </li>
                                  <li><a href="#level2_2">Level Two</a>
                                  </li>
                                </ul>
                              </li>
                              <li><a href="#level1_2">Level One</a>
                              </li>
                          </ul>
                        </li>
                        <li><a href="javascript:void(0)"><i class="fa fa-laptop"></i> Landing Page <span class="label label-success pull-right">Coming Soon</span></a></li>
                      </ul>
                    </div-->

                </div>
                <!-- /sidebar menu -->

                <!-- /menu footer buttons -->
                <!--div class="sidebar-footer hidden-small">
                  <a data-toggle="tooltip" data-placement="top" title="Settings">
                    <span class="glyphicon glyphicon-cog" aria-hidden="true"></span>
                  </a>
                  <a data-toggle="tooltip" data-placement="top" title="FullScreen">
                    <span class="glyphicon glyphicon-fullscreen" aria-hidden="true"></span>
                  </a>
                  <a data-toggle="tooltip" data-placement="top" title="Lock">
                    <span class="glyphicon glyphicon-eye-close" aria-hidden="true"></span>
                  </a>
                  <a data-toggle="tooltip" data-placement="top" title="Logout">
                    <span class="glyphicon glyphicon-off" aria-hidden="true"></span>
                  </a>
                </div-->
                <!-- /menu footer buttons -->
            </div>
        </div>

        <!-- top navigation -->
        <div class="top_nav">
            <div class="nav_menu">
                <nav class="" role="navigation">
                    <div class="nav toggle">
                        <a id="menu_toggle"><i class="fa fa-bars"></i></a>
                    </div>

                    <!--ul class="nav navbar-nav navbar-right">
                      <li class="">
                        <a href="javascript:;" class="user-profile dropdown-toggle" data-toggle="dropdown" aria-expanded="false">
                          <img src="images/img.jpg" alt="">John Doe
                          <span class=" fa fa-angle-down"></span>
                        </a>
                        <ul class="dropdown-menu dropdown-usermenu pull-right">
                          <li><a href="javascript:;"> Profile</a></li>
                          <li>
                            <a href="javascript:;">
                              <span class="badge bg-red pull-right">50%</span>
                              <span>Settings</span>
                            </a>
                          </li>
                          <li><a href="javascript:;">Help</a></li>
                          <li><a href="login.html"><i class="fa fa-sign-out pull-right"></i> Log Out</a></li>
                        </ul>
                      </li>

                      <li role="presentation" class="dropdown">
                        <a href="javascript:;" class="dropdown-toggle info-number" data-toggle="dropdown" aria-expanded="false">
                          <i class="fa fa-envelope-o"></i>
                          <span class="badge bg-green">6</span>
                        </a>
                        <ul id="menu1" class="dropdown-menu list-unstyled msg_list" role="menu">
                          <li>
                            <a>
                              <span class="image"><img src="images/img.jpg" alt="Profile Image" /></span>
                              <span>
                                <span>John Smith</span>
                                <span class="time">3 mins ago</span>
                              </span>
                              <span class="message">
                                Film festivals used to be do-or-die moments for movie makers. They were where...
                              </span>
                            </a>
                          </li>
                          <li>
                            <a>
                              <span class="image"><img src="images/img.jpg" alt="Profile Image" /></span>
                              <span>
                                <span>John Smith</span>
                                <span class="time">3 mins ago</span>
                              </span>
                              <span class="message">
                                Film festivals used to be do-or-die moments for movie makers. They were where...
                              </span>
                            </a>
                          </li>
                          <li>
                            <a>
                              <span class="image"><img src="images/img.jpg" alt="Profile Image" /></span>
                              <span>
                                <span>John Smith</span>
                                <span class="time">3 mins ago</span>
                              </span>
                              <span class="message">
                                Film festivals used to be do-or-die moments for movie makers. They were where...
                              </span>
                            </a>
                          </li>
                          <li>
                            <a>
                              <span class="image"><img src="images/img.jpg" alt="Profile Image" /></span>
                              <span>
                                <span>John Smith</span>
                                <span class="time">3 mins ago</span>
                              </span>
                              <span class="message">
                                Film festivals used to be do-or-die moments for movie makers. They were where...
                              </span>
                            </a>
                          </li>
                          <li>
                            <div class="text-center">
                              <a>
                                <strong>See All Alerts</strong>
                                <i class="fa fa-angle-right"></i>
                              </a>
                            </div>
                          </li>
                        </ul>
                      </li>
                    </ul-->
                </nav>
            </div>
        </div>
        <!-- /top navigation -->

        <!-- page content -->
        <div class="right_col" role="main">
            <div class="">
                <div class="page-title">
                    <div class="title_left">
                        <h3>Contract Parser
                            <small>Copy &amp; paste your inventory</small>
                        </h3>
                    </div>

                    <!--div class="title_right">
                      <div class="col-md-5 col-sm-5 col-xs-12 form-group pull-right top_search">
                        <div class="input-group">
                          <input type="text" class="form-control" placeholder="Search for...">
                          <span class="input-group-btn">
                            <button class="btn btn-default" type="button">Go!</button>
                          </span>
                        </div>
                      </div>
                    </div-->
                </div>

                <div class="clearfix"></div>

                <div class="row">

                    <div class="col-md-12 col-sm-12 col-xs-12">
                        <div class="x_panel">
                            <div class="x_title">
                                <h2>Contract Items</h2>
                                <ul class="nav navbar-right panel_toolbox">
                                    <!--li>
                                        <a class="collapse-link"><i class="fa fa-chevron-up"></i></a>
                                    </li-->
                                    <!--li class="dropdown">
                                        <a href="#" class="dropdown-toggle" data-toggle="dropdown" role="button"
                                           aria-expanded="false"><i class="fa fa-wrench"></i></a>
                                        <ul class="dropdown-menu" role="menu">
                                            <li><a href="#">Settings 1</a>
                                            </li>
                                            <li><a href="#">Settings 2</a>
                                            </li>
                                        </ul>
                                    </li-->
                                    <!--li>
                                        <a class="close-link"><i class="fa fa-close"></i></a>
                                    </li-->
                                </ul>
                                <div class="clearfix"></div>
                            </div>
                            <div class="x_content">
                                <p class="text-muted font-13 m-b-30">
                                    Howto goes here...
                                </p>

                                <form class="form-horizontal form-label-left input_mask" method="post" id="contractData">
                                    <div class="form-group">
                                        <textarea name="textAreaContract" id="textAreaContract" class="resizable_textarea form-control">{{inputdata}}</textarea>
                                    </div>
                                    <div class="form-group">
                                        <button class="btn btn-primary" id="reset" type="reset">Reset</button>
                                        <button class="btn btn-success" id="submit" type="submit">Calculate</button>
                                    </div>
                                </form>
                            </div>
                        </div>
                    </div>

                    % if result is not None:
                        <div class="col-md-12 col-sm-12 col-xs-12">
                            <div class="x_panel">
                                <div class="x_title">
                                    <h2>Results</h2>
                                    <ul class="nav navbar-right panel_toolbox">
                                        <!--li>
                                            <a class="collapse-link"><i class="fa fa-chevron-up"></i></a>
                                        </li-->
                                        <!--li class="dropdown">
                                            <a href="#" class="dropdown-toggle" data-toggle="dropdown" role="button"
                                               aria-expanded="false"><i class="fa fa-wrench"></i></a>
                                            <ul class="dropdown-menu" role="menu">
                                                <li><a href="#">Settings 1</a>
                                                </li>
                                                <li><a href="#">Settings 2</a>
                                                </li>
                                            </ul>
                                        </li-->
                                        <!--li><a class="close-link"><i class="fa fa-close"></i></a>
                                        </li-->
                                    </ul>
                                    <div class="clearfix"></div>
                                </div>
                                <div class="x_content">
                                    <table id="datatable-buttons" class="table table-striped table-bordered">
                                        <thead>
                                        <tr>
                                            <th>Name</th>
                                            <th>Id</th>
                                            <th>Jita Min Buy</th>
                                            <th>Jita Max Buy</th>
                                            <th>Jita Min Sell</th>
                                            <th>Jita Max Sell</th>
                                            <th>Corp Buy price</th>
                                        </tr>
                                        </thead>
                                        <tbody>
                                        % for line in result['price_table']:
                                        <tr>
                                            <td>{{line['typeName']}}</td>
                                            <td class="dt-body-right">{{line['typeID']}}</td>
                                            <td class="dt-body-right">{{line['min_buy_price']}}</td>
                                            <td class="dt-body-right">{{line['max_buy_price']}}</td>
                                            <td class="dt-body-right">{{line['min_sell_price']}}</td>
                                            <td class="dt-body-right">{{line['max_sell_price']}}</td>
                                            <td class="dt-body-right"><strong>{{'{:0.2f}'.format(line['max_buy_price'] * 0.95)}}</strong></td>
                                        </tr>
                                        % end
                                        </tbody>
                                        <tfoot>
                                        <tr>
                                            <td style="border-top: 2px solid"><strong>Sum</strong></td>
                                            <td class="dt-body-right" style="border-top: 2px solid">&nbsp;</td>
                                            <td class="dt-body-right" style="border-top: 2px solid">&nbsp;</td>
                                            <td class="dt-body-right" style="border-top: 2px solid">&nbsp;</td>
                                            <td class="dt-body-right" style="border-top: 2px solid">&nbsp;</td>
                                            <td class="dt-body-right" style="border-top: 2px solid">&nbsp;</td>
                                            <td class="dt-body-right" style="border-top: 2px solid">
                                                <strong>{{result['sum']}}</strong>
                                            </td>
                                        </tr>
                                        </tfoot>
                                    </table>
                                </div>
                            </div>
                        </div>
                    % end

                    % if output:
                        <div class="col-md-12 col-sm-12 col-xs-12">
                            <div class="x_panel">
                                <div class="x_title">
                                    <h2>Results</h2>
                                    <ul class="nav navbar-right panel_toolbox">
                                        <!--li>
                                            <a class="collapse-link"><i class="fa fa-chevron-up"></i></a>
                                        </li-->
                                        <!--li class="dropdown">
                                            <a href="#" class="dropdown-toggle" data-toggle="dropdown" role="button"
                                               aria-expanded="false"><i class="fa fa-wrench"></i></a>
                                            <ul class="dropdown-menu" role="menu">
                                                <li><a href="#">Settings 1</a>
                                                </li>
                                                <li><a href="#">Settings 2</a>
                                                </li>
                                            </ul>
                                        </li-->
                                        <!--li><a class="close-link"><i class="fa fa-close"></i></a>
                                        </li-->
                                    </ul>
                                    <div class="clearfix"></div>
                                </div>
                                <div class="x_content">
                                    <div class="alert alert-info">
                                        <pre>
                                            {{output}}
                                        </pre>
                                    </div>
                                </div>
                            </div>
                        </div>
                    % end

                </div>
            </div>
        </div>
        <!-- /page content -->

        <!-- footer content -->
        <footer>
            <div class="pull-right">
                TRAGU Tools by chocokiko aka "Estela Gatita-Nina"<br/>
                Gentelella - Bootstrap Admin Template by <a href="https://colorlib.com">Colorlib</a>
            </div>
            <div class="clearfix"></div>
        </footer>
        <!-- /footer content -->
    </div>
</div>

<!-- jQuery -->
<script src="/static/node_modules/gentelella/vendors/jquery/dist/jquery.min.js"></script>
<!-- Bootstrap -->
<script src="/static/node_modules/gentelella/vendors/bootstrap/dist/js/bootstrap.min.js"></script>
<!-- FastClick -->
<script src="/static/node_modules/gentelella/vendors/fastclick/lib/fastclick.js"></script>
<!-- NProgress -->
<script src="/static/node_modules/gentelella/vendors/nprogress/nprogress.js"></script>
<!-- Datatables -->
<script src="/static/node_modules/gentelella/vendors/datatables.net/js/jquery.dataTables.min.js"></script>
<script src="/static/node_modules/gentelella/vendors/datatables.net-bs/js/dataTables.bootstrap.min.js"></script>
<script src="/static/node_modules/gentelella/vendors/datatables.net-buttons/js/dataTables.buttons.min.js"></script>
<script src="/static/node_modules/gentelella/vendors/datatables.net-buttons-bs/js/buttons.bootstrap.min.js"></script>
<script src="/static/node_modules/gentelella/vendors/datatables.net-buttons/js/buttons.flash.min.js"></script>
<script src="/static/node_modules/gentelella/vendors/datatables.net-buttons/js/buttons.html5.min.js"></script>
<script src="/static/node_modules/gentelella/vendors/datatables.net-buttons/js/buttons.print.min.js"></script>
<script src="/static/node_modules/gentelella/vendors/datatables.net-fixedheader/js/dataTables.fixedHeader.min.js"></script>
<script src="/static/node_modules/gentelella/vendors/datatables.net-keytable/js/dataTables.keyTable.min.js"></script>
<script src="/static/node_modules/gentelella/vendors/datatables.net-responsive/js/dataTables.responsive.min.js"></script>
<script src="/static/node_modules/gentelella/vendors/datatables.net-responsive-bs/js/responsive.bootstrap.js"></script>
<script src="/static/node_modules/gentelella/vendors/datatables.net-scroller/js/dataTables.scroller.min.js"></script>
<script src="/static/node_modules/gentelella/vendors/jszip/dist/jszip.min.js"></script>
<script src="/static/node_modules/gentelella/vendors/pdfmake/build/pdfmake.min.js"></script>
<script src="/static/node_modules/gentelella/vendors/pdfmake/build/vfs_fonts.js"></script>

<!-- Custom Theme Scripts -->
<script src="/static/node_modules/gentelella/build/js/custom.min.js"></script>

<!-- Datatables -->
<script>
      $(document).ready(function() {
        var handleDataTableButtons = function() {
          if ($("#datatable-buttons").length) {
            $("#datatable-buttons").DataTable({
              dom: "Bfrtip",
              buttons: [
                {
                  extend: "copy",
                  className: "btn-sm"
                },
                {
                  extend: "csv",
                  className: "btn-sm"
                },
                {
                  extend: "excel",
                  className: "btn-sm"
                },
                {
                  extend: "pdfHtml5",
                  className: "btn-sm"
                },
                {
                  extend: "print",
                  className: "btn-sm"
                },
              ],
              responsive: true,
              keys: true
            });
          }
        };

        TableManageButtons = function() {
          "use strict";
          return {
            init: function() {
              handleDataTableButtons();
            }
          };
        }();

        TableManageButtons.init();
      });

</script>
<!-- /Datatables -->
</body>
</html>