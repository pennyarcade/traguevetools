<%
    rebase('skeleton.html.tpl', page=page)
%>

<div class="col-md-9 col-sm-9 col-xs-12">
    <div class="x_panel fixed_height_390">
        <div class="x_title">
            <h2>Dear NETG friends and fellow capsuleers,</h2>
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
            <p>developing this app costs a lot of time and also real life money.
               Please help me to give you the best tool I can possibly offer by
               helping me offset the hosting costs. The development will be free :-)<p>
            <p>The server costs me <strong>$60 a year or $5.50 a month</strong>.
               The plan is simple,
               Donate ISK to "Scrooge TheTreasurer" in game. I'll buy PLEX to lower
               RL Money costs for subbing. The saved money will be used for hosting costs
               instead.<p>
            <p>As an incentive I offer Kickstarter like goals depending on donation level
               for the current year. All donations and the complete wallet journal of
               Scrooge will be displayed below for transparency. Also there are highscores below.
            </p>
            <pre>
                $60 -> 1400 PLEX
                1 PLEX is roughly 2.7 mil ISK
                $60 -> 3.780 bil ISK a year</pre>
            <p>Those numbers may sound like much but it is distributed over a whole year
               and many shoulders. If only 10 people donate 7 mil a week it would already work.</p>
        </div>
    </div>
</div>
<div class="col-md-3 col-sm-3 col-xs-12 widget widget_tally_box">
    <div class="x_panel fixed_height_390">
      <div class="x_title">
        <h2>Total progress</h2>
        <div class="clearfix"></div>
      </div>
      <div class="x_content">
        <div style="text-align: center; margin-bottom: 17px">
          <span class="chart" data-percent="6{{page['result']['statistics']['percentage']}}">
              <span class="percent"></span>
          </span>
        </div>

        <h3 class="name_title">Thank you</h3>
        <p>For your donations</p>

        <div class="divider"></div>

        <p><center>
          {{page['result']['statistics']['total_donations']}}<br/>
          of<br/>
          {{page['result']['statistics']['hosting_costs']}}<br/>
          donated.
        </center></p>

      </div>
    </div>
</div>

<div class="col-md-12 col-sm-12 col-xs-12">
    <div class="x_panel">
        <div class="x_title">
            <h2>Donation goals (7.2017 - 7.2018)</h2>
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
            <table id="datatable-journal" class="table table-striped table-bordered">
                <thead>
                <tr>
                    <th>Milestone</th>
                    <th>Amount</th>
                    <th>Progress</th>
                    <th>Features</th>
                </tr>
                </thead>
                <tbody>
                % for name, stone in page['result']['milestones'].iteritems():
                <tr style="">
                    <td>{{name}}</td>
                    <td class="dt-body-right">{{stone['amount']}}</td>
                    <td class="dt-body-right"></td>
                    <td>
                        % for issue in stone['issues']:
                            <a href="/development/{{issue['local_id']}}/">{{issue['title']}}</a><br/>
                        % end
                    </td>
                </tr>
                % end
                </tbody>
            </table>
        </div>
    </div>
</div>

<div class="col-md-3 col-sm-3 col-xs-12 widget widget_tally_box">
    <div class="x_panel fixed_height_390">
      <div class="x_title">
        <h2>Best donors</h2>
        <div class="clearfix"></div>
      </div>
      <div class="x_content">
        <div style="text-align: center; margin-bottom: 17px">
          <center>
              <h5>#1</h5>
              <img src="http://image.eveonline.com/Character/97082031_128.jpg"><br/>
              <h5>1235 mil</h5>
          </center>
        </div>

        <div class="divider"></div>

        <div>
            <ul class="list-inline widget_tally">
                <li>
                    <p>
                        <span class="count">#2</span>
                        <span class="count"><img src="http://image.eveonline.com/Character/93930393_32.jpg"></span>
                        <span class="count">256 mil</span>
                    </p>
                </li>
                <li>
                    <p>
                        <span class="count">#3</span>
                        <span class="count"><img src="http://image.eveonline.com/Character/91434341_32.jpg"></span>
                        <span class="count">22 mil</span>
                    </p>
                </li>
            </ul>
        </div>

      </div>
    </div>
</div>
<div class="col-md-3 col-sm-3 col-xs-12 widget widget_tally_box">
    <div class="x_panel fixed_height_390">
      <div class="x_title">
        <h2>Latest donors</h2>
        <div class="clearfix"></div>
      </div>
      <div class="x_content">
        <div style="text-align: center; margin-bottom: 17px">
          <center>
              <h5>8.07.2015 08:50</h5>
              <img src="http://image.eveonline.com/Character/97082031_128.jpg"><br/>
              <h5>1235 mil</h5>
          </center>
        </div>

        <div class="divider"></div>

        <div>
            <ul class="list-inline widget_tally">
                <li>
                    <p>
                        <span class="count">8.07.2015 08:50</span>
                        <span class="count"><img src="http://image.eveonline.com/Character/91434341_32.jpg"></span>
                        <span class="count">256 mil</span>
                    </p>
                </li>
                <li>
                    <p>
                        <span class="count">8.07.2015 08:50</span>
                        <span class="count"><img src="http://image.eveonline.com/Character/93930393_32.jpg"></span>
                        <span class="count">22 mil</span>
                    </p>
                </li>
            </ul>
        </div>

      </div>
    </div>
</div>
<div class="col-md-3 col-sm-3 col-xs-12 widget widget_tally_box">
    <div class="x_panel fixed_height_390">
      <div class="x_title">
        <h2>Highest single donation</h2>
        <div class="clearfix"></div>
      </div>
      <div class="x_content">
        <div style="text-align: center; margin-bottom: 17px">
          <span>
              <img src="http://image.eveonline.com/Character/93930393_128.jpg">
          </span>
        </div>

        <h3 class="name_title">56 mil</h3>
        <p>donated</p>

        <div class="divider"></div>

        <p>you are the bestest, thank you soo much</p>

      </div>
    </div>
</div>
<div class="col-md-3 col-sm-3 col-xs-12 widget widget_tally_box">
    <div class="x_panel fixed_height_390">
      <div class="x_title">
        <h2>Donor of the month</h2>
        <div class="clearfix"></div>
      </div>
      <div class="x_content">
        <div style="text-align: center; margin-bottom: 17px">
          <span>
              <img src="http://image.eveonline.com/Character/93930393_128.jpg">
          </span>
        </div>

        <h3 class="name_title">56 mil</h3>
        <p>donated</p>

        <div class="divider"></div>

        <p>you are the bestest, thank you soo much</p>

      </div>
    </div>
</div>

<div class="col-md-12 col-sm-12 col-xs-12">
    <div class="x_panel">
        <div class="x_title">
            <h2>Wallet Journal (7.2017 - 7.2018)</h2>
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
            <table id="datatable-journal" class="table table-striped table-bordered">
                <thead>
                <tr>
                    <th>Date</th>
                    <th>ID</th>
                    <th>Type</th>
                    <th>Amount</th>
                    <th>Balance</th>
                    <th>From</th>
                    <th>To</th>
                    <th>Tax</th>
                    <th>Reason</th>
                </tr>
                </thead>
                <tbody>
                % for line in page['result']['journal_table']:
                <tr style="">
                    <td>{{line['date']}}</td>
                    <td class="dt-body-right">{{line['refID']}}</td>
                    <td class="dt-body-right">{{line['refTypeID']}}</td>
                    <td class="dt-body-right">{{line['amount'] if line.has_key('amount') else ''}}</td>
                    <td class="dt-body-right">{{line['balance'] if line.has_key('balance') else ''}}</td>
                    <td class="dt-body-right">{{line['firstPartyID'] if line.has_key('firstPartyID') else ''}}</td>
                    <td class="dt-body-right">{{line['secondPartyID'] if line.has_key('secondPartyID') else ''}}</td>
                    <td class="dt-body-right">{{line['taxAmount'] if line.has_key('taxAmount') else ''}}</td>
                    <td class="dt-body-right">{{line['reason'] if line.has_key('reason') else ''}}</td>
                </tr>
                % end
                </tbody>
            </table>
        </div>
    </div>
</div>
