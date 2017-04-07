<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>Contract Parser</title>
	<link href="jquery/jquery-ui.css" rel="stylesheet">
	<style>
        body{
            font-family: "Trebuchet MS", sans-serif;
            margin: 50px;
        }
        .demoHeaders {
            margin-top: 2em;
        }
        #dialog-link {
            padding: .4em 1em .4em 20px;
            text-decoration: none;
            position: relative;
        }
        #dialog-link span.ui-icon {
            margin: 0 5px 0 0;
            position: absolute;
            left: .2em;
            top: 50%;
            margin-top: -8px;
        }
        #icons {
            margin: 0;
            padding: 0;
        }
        #icons li {
            margin: 2px;
            position: relative;
            padding: 4px 0;
            cursor: pointer;
            float: left;
            list-style: none;
        }
        #icons span.ui-icon {
            float: left;
            margin: 0 4px;
        }
        .fakewindowcontain .ui-widget-overlay {
            position: absolute;
        }
        select {
            width: 200px;
        }
	</style>
</head>
<body>
    <h2>TRAGU Contract Parser</h2>
    <form method="post" id="contractData">
        <center>
            <label form="contractData">Contract Items</label><br/>
            <textarea cols="80" rows="20" name="textAreaContract" id="textAreaContract">
                Copy contract items here
            </textarea><br/>
            <button type="reset">Reset</button><br/>
            <button type="submit">Calculate</button><br/>
        </center>
    </form>

    % if result is not None:
    <hr/>
    <table>
        <thead>
            <tr>
                <th>Name</th>
                <th>Id</th>
                <th>Jita Buy</th>
                <th>Jita Sell</th>
                <th>Median</th>
            </tr>
        </thead>
        <tbody>
            % for line in result:
                <tr>
                    <td>{{line['itemName']}}</td>
                    <td>{{line['itemId']}}</td>
                    <td>{{line['jitaBuy']}}</td>
                    <td>{{line['jitaSell']}}</td>
                    <td>{{line['median']}}</td>
                </tr>
            % end
        </tbody>
    </table>
    % end
</body>
</html>