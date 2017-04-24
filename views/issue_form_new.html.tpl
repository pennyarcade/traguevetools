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
        <form class="form-horizontal form-label-left input_mask" name="create_issue" method="POST" id="create_issue_form">
          <input
                id="form"
                value="new_issue"
                type="hidden"
                name="form"
          />
          <div class="modal-content">
            <div class="modal-header">
              <button type="button" class="close" data-dismiss="modal">
                <span aria-hidden="true">×</span>
              </button>
              <h4 class="modal-title" id="myModalLabel">Create Issue</h4>
            </div>
              <div class="modal-body">
                <div class="col-md-6 col-sm-6 col-xs-12 form-group has-feedback">
                  <label>&nbsp;</label>
                  <input
                          class="form-control has-feedback-left"
                          placeholder="Ingame name"
                          type="text"
                          name="issue_name"
                          id="issue_name"
                  />
                  <span class="fa fa-user form-control-feedback left" aria-hidden="true"></span>
                </div>
                <div class="col-md-2 col-sm-2 col-xs-12 form-group has-feedback">
                  <label>Component</label>
                  <select class="form-control" name="issue_component" id="issue_component">
                    <option selected="selected">Contract Parser</option>
                    <option>Development Page</option>
                    <option>Overview Dashboard</option>
                  </select>
                </div>
                <div class="col-md-2 col-sm-2 col-xs-12 form-group has-feedback">
                  <label>Priority</label>
                  <select class="form-control" name="issue_priority" id="issue_priority">
                    <option selected="selected">trivial</option>
                    <option>minor</option>
                    <option>major</option>
                    <option>critical</option>
                    <option>blocker</option>
                  </select>
                </div>
                <div class="col-md-2 col-sm-2 col-xs-12 form-group has-feedback">
                  <label>Kind</label>
                  <select class="form-control" name="issue_kind" id="issue_kind">
                    <option selected="selected">bug</option>
                    <option>enhancement</option>
                    <option>proposal</option>
                    <option>task</option>
                  </select>
                </div>

                <div class="col-md-12 col-sm-12 col-xs-12 form-group">
                    <input
                            class="form-control has-feedback-left"
                            aria-label="Subject"
                            type="text"
                            placeholder="Subject"
                            name="issue_subject"
                            id="issue_subject"
                    />
                    <span class="fa fa-envelope form-control-feedback left" aria-hidden="true"></span>
                </div>

                <div class="col-md-12 col-sm-12 col-xs-12 form-group">
                  <label>Content</label>
                  <textarea
                          id="issue_content"
                          class="form-control markitup"
                          rows="10"
                          placeholder="Content"
                          name="issue_content"
                  ></textarea>
                </div>
              </div>
            <div class="modal-footer">
              <button type="button" class="btn btn-default" data-dismiss="modal">Close</button>
              <button type="submit" class="btn btn-primary">Save changes</button>
            </div>
          </div>
        </form>
      </div>
    </div>
% end