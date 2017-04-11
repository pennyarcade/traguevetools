<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>Contract Parser</title>
	<link href="/static/jquery/jquery-ui.css" rel="stylesheet">
	<style>
        body{
            font-family: "Trebuchet MS", sans-serif;
            margin: 50px;
            background-color: #ccc;
        }
        td {
            margin: 3px;
        }
        table thead td, table thead td {
            border: 1px solid;
        }
	</style>
</head>
<body>
    <h2>TRAGU Contract Parser</h2>
    <form method="post" id="contractData">
        <fieldset>
        	<legend>Contract Items</legend>
            <textarea cols="80" rows="20" name="textAreaContract" id="textAreaContract">{{inputdata}}</textarea><br/>
            <button id="reset" type="reset">Reset</button>
            <button id="submit" type="submit">Calculate</button><br/>
        </fieldset>
    </form>

    % if result is not None:
    <hr/>
    <table>
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
                    <td>{{line['typeID']}}</td>
                    <td>{{line['min_buy_price']}}</td>
                    <td>{{line['max_buy_price']}}</td>
                    <td>{{line['min_sell_price']}}</td>
                    <td>{{line['max_sell_price']}}</td>
                    <td><strong>{{line['max_buy_price'] / 0.95}}</strong></td>
                </tr>
            % end
        </tbody>
        <tfoot>
            <tr>
                <td>&nbsp;</td>
                <td>&nbsp;</td>
                <td>&nbsp;</td>
                <td>&nbsp;</td>
                <td>&nbsp;</td>
                <td>&nbsp;</td>
                <td style="border-top: 2px solid">
                    <strong>&Sigma; {{result['sum']}}</strong>
                </td>
            </tr>
        </tfoot>
    </table>
    % end
    % if output:
    <hr/>
    <div class="ui-widget">
	    <div class="ui-state-highlight ui-corner-all" style="margin-top: 20px; padding: 0 .7em;">
		    <p><span class="ui-icon ui-icon-info" style="float: left; margin-right: .3em;"></span><br/>
                <pre>{{output}}</pre>
		    </p>
	    </div>
    </div>
    % end
</body>
</html>