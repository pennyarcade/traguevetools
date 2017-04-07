<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>Contract Parser</title>
    <style>
        table, td, th {
            border: 1px solid black;
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