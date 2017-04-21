<button
   id="compose"
   class="btn btn-sm btn-success btn-block"
   type="button"
   data-toggle="modal"
   data-target=".create-modal-lg"
>Create Issue</button>
% if not only_button:
    <div class="modal fade create-modal-lg" tabindex="-1" role="dialog" aria-hidden="true" style="display: none;">
      <div class="modal-dialog modal-lg">
        <div class="modal-content">
          <form method="POST">
            <div class="modal-header">
              <button type="button" class="close" data-dismiss="modal">
                <span aria-hidden="true">×</span>
              </button>
              <h4 class="modal-title" id="myModalLabel">Create Issue</h4>
            </div>
            <div class="modal-body">
              <form class="form-horizontal form-label-left input_mask" name="create_issue">
                <div class="col-md-6 col-sm-6 col-xs-12 form-group has-feedback">
                  <label>&nbsp;</label>
                  <input id="name" class="form-control has-feedback-left" placeholder="Ingame name" type="text"/>
                  <span class="fa fa-user form-control-feedback left" aria-hidden="true"></span>
                </div>
                <div class="col-md-2 col-sm-2 col-xs-12 form-group has-feedback">
                  <label>Component</label>
                  <select class="form-control">
                    <option value="">Component</option>
                    <option>Contract Parser</option>
                    <option>Development Page</option>
                    <option>Overview Dashboard</option>
                  </select>
                </div>
                <div class="col-md-2 col-sm-2 col-xs-12 form-group has-feedback">
                  <label>Priority</label>
                  <select class="form-control">
                    <option value="">Priority</option>
                    <option>trivial</option>
                    <option>minor</option>
                    <option>major</option>
                    <option>critical</option>
                    <option>blocker</option>
                  </select>
                </div>
                <div class="col-md-2 col-sm-2 col-xs-12 form-group has-feedback">
                  <label>Kind</label>
                  <select class="form-control">
                    <option value="">Kind</option>
                    <option>bug</option>
                    <option>enhancement</option>
                    <option>proposal</option>
                    <option>task</option>
                  </select>
                </div>

                <div class="col-md-12 col-sm-12 col-xs-12 form-group">
                    <input class="form-control has-feedback-left" aria-label="Subject" type="text" placeholder="Subject"/>
                    <span class="fa fa-envelope form-control-feedback left" aria-hidden="true"></span>
                </div>

                <div class="col-md-12 col-sm-12 col-xs-12 form-group">
                  <label>Content</label>
                  <textarea id="issue_content" class="form-control markitup" rows="10" placeholder="Content"></textarea>
                </div>
              </form>
            </div>
            <div class="modal-footer">
              <button type="button" class="btn btn-default" data-dismiss="modal">Close</button>
              <button type="submit" class="btn btn-primary">Save changes</button>
            </div>
          </form>
        </div>
      </div>
    </div>
% end