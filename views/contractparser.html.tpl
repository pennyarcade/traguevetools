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
            <h4>How to use this page:</h4>
            <p class="text-muted font-13 m-b-30">
                <ol>
                    <li>Select all items want to sell to the corporation in your inventory</li>
                    <li>Press <strong>CTRL+C</strong> to copy</li>
                    <li>Switch to your browser and open this page</li>
                    <li>Click into the textbox below and press <strong>CTRL+V</strong> to paste</li>
                    <li>Click "Calculate"</li>
                    <li>Select and copy the total value at the bottom of the table</li>
                    <li>Switch back to the game</li>
                    <li>Rightclick the selected inventory entries and select "Create Contract"</li>
                    <li>Select "Item Exchange" and "My Corporation" and click "Next"</li>
                    <li>Review items and click "Next"</li>
                    <li>Paste the calculated value from above into "I will recieve"</li>
                    <li>Add a sensible Description like "Ore buyback"</li>
                    <li>Set expiration to 2 weeks and click "Next"</li>
                    <li>Review the contract settings abd click "Finish"</li>
                    <li>Wait for our buyers to complete the transaction.</li>
                </ol>
            </p>

            <form class="form-horizontal form-label-left input_mask" method="post" id="contractData">
                <div class="form-group">
                    <textarea name="textAreaContract" id="textAreaContract" class="resizable_textarea form-control">{{page['input_data'] if page['input_data'] is not None else '' }}</textarea>
                </div>
                <div class="form-group">
                    <button class="btn btn-primary" id="reset" type="reset">Reset</button>
                    <button class="btn btn-success" id="submit" type="submit">Calculate</button>
                </div>
            </form>
        </div>
    </div>
</div>

% if page['result'] is not None:
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
                    % for line in page['result']['price_table']:
                    <tr style="{{'background-color:#f88;' if not line.has_key('max_buy_price') else ''}}">
                        <td>{{line['typeName']}}</td>
                        <td class="dt-body-right">{{line['amount']}}</td>
                        <td class="dt-body-right">{{line['min_buy_price'] if line.has_key('min_buy_price') else ''}}</td>
                        <td class="dt-body-right">{{get(line['max_buy_price'] if line.has_key('max_buy_price') else '')}}</td>
                        <td class="dt-body-right">{{get(line['min_sell_price'] if line.has_key('min_sell_price') else '')}}</td>
                        <td class="dt-body-right">{{get(line['max_sell_price'] if line.has_key('max_sell_price') else '')}}</td>
                        <td class="dt-body-right">{{'{:,.2f}'.format(line['corp_buy']) if line.get('corp_buy') else 'None'}}</td>
                        <td class="dt-body-right"><strong>{{'{:,.2f}'.format(line['corp_buy_total']) if line.get('corp_buy_total') else 'None'}}</strong></td>
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
                            <strong>{{'{:,.2f}'.format(page['result']['sum'])}}</strong>
                        </td>
                    </tr>
                    </tfoot>
                </table>
            </div>
        </div>
    </div>
% end

