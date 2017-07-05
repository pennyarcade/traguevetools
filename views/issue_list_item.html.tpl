<%
    if issue['metadata']['kind'] == 'bug':
        kclass = 'fa-bug'
    elif issue['metadata']['kind'] == 'enhancement':
        kclass = 'fa-lightbulb-o'
    elif issue['metadata']['kind'] == 'proposal':
        kclass = 'fa-comment'
    elif issue['metadata']['kind'] == 'task':
        kclass = 'fa-wrench'
    else:
        kclass = 'fa-square-o'
    end

    if issue['priority'] == 'trivial':
        pclass = 'fa-smile-o'
    elif issue['priority'] == 'minor':
        pclass = 'fa-meh-o'
    elif issue['priority'] == 'major':
        pclass = 'fa-frown-o'
    elif issue['priority'] == 'critical':
        pclass = 'fa-exclamation'
    elif issue['priority'] == 'blocker':
        pclass = 'fa-bolt'
    else:
        pclass = 'fa-square-o'
    end
%>
<a href="/development/{{issue['local_id']}}/">
  <div class="mail_list">
    <div class="left">
      % if issue['metadata']['kind']:
        <i class="fa {{get('kclass')}}" title="{{issue['metadata']['kind']}}"></i>
      % end
      % if issue['priority']:
        <i class="fa {{get('pclass')}}" title="{{issue['priority']}}"></i>
      % end
    </div>
    <div class="right">
      <h3>
          <span class="image">
            <img src="{{issue['reported_by']['avatar']}}" alt="[img]">
          </span>

          {{issue['reported_by']['display_name']}} <small>{{issue['utc_created_on'].strftime('%y-%m-%d %H:%M')}}</small>
      </h3>
      <p><span class="badge">{{issue['status']}}</span>&nbsp;{{issue['title']}}</p>
    </div>
  </div>
</a>