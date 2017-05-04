<%
    rebase('skeleton.html.tpl', page=page)
%>

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
                    <textarea name="textAreaContract" id="textAreaContract" class="resizable_textarea form-control">{{page[inputdata}}</textarea>
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
                        <th>Amount</th>
                        <th>Jita Min Buy</th>
                        <th>Jita Max Buy</th>
                        <th>Jita Min Sell</th>
                        <th>Jita Max Sell</th>
                        <th>Corp Buy price</th>
                        <th>Corp Buy total</th>
                    </tr>
                    </thead>
                    <tbody>
                    % for line in result['price_table']:
                    <tr style="{{'background-color:#f88;' if not line['max_buy_price'] else ''}}">
                        <td>{{line['typeName']}}</td>
                        <td class="dt-body-right">{{line['amount']}}</td>
                        <td class="dt-body-right">{{line['min_buy_price']}}</td>
                        <td class="dt-body-right">{{line['max_buy_price']}}</td>
                        <td class="dt-body-right">{{line['min_sell_price']}}</td>
                        <td class="dt-body-right">{{line['max_sell_price']}}</td>
                        <td class="dt-body-right">{{'{:0.2f}'.format(line['corp_buy']) if line['corp_buy'] else 'None'}}</td>
                        <td class="dt-body-right"><strong>{{'{:0.2f}'.format(line['corp_buy_total']) if line['corp_buy_total'] else 'None'}}</strong></td>
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
                        <td class="dt-body-right" style="border-top: 2px solid">&nbsp;</td>
                        <td class="dt-body-right" style="border-top: 2px solid">
                            <strong>{{'{:0.2f}'.format(result['sum'])}}</strong>
                        </td>
                    </tr>
                    </tfoot>
                </table>
            </div>
        </div>
    </div>
% end

