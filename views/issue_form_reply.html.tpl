<div class="btn-group">
  <button
    class="btn btn-sm btn-primary"
    type="button"
    data-toggle="modal"
    data-target=".reply-modal-lg"
  >
      <i class="fa fa-reply"></i> Reply
  </button>
</div>

% if not only_button:
  <div class="modal fade reply-modal-lg" tabindex="-1" role="dialog" aria-hidden="true" style="display: none;">
    <div class="modal-dialog modal-lg">
      <form
              class="form-horizontal form-label-left input_mask"
              name="reply_issue"
              method="PUT"
              id="reply_issue"
      >
        <input
                id="form"
                value="reply_issue"
                type="hidden"
                name="form"
        />
        <div class="modal-content">
          <div class="modal-header">
            <button type="button" class="close" data-dismiss="modal">
              <span aria-hidden="true">×</span>
            </button>
            <h4 class="modal-title" id="myModalLabel">Reply to Issue</h4>
          </div>
          <div class="modal-body">
              <div class="col-md-6 col-sm-6 col-xs-12 form-group has-feedback">
                <label>&nbsp;</label>
                <input
                        id="reply_name"
                        class="form-control has-feedback-left"
                        placeholder="Ingame name"
                        type="text"
                        name="reply_name"
                />
                <span class="fa fa-user form-control-feedback left" aria-hidden="true"></span>
              </div>

              <div class="col-md-12 col-sm-12 col-xs-12 form-group">
                <label>Content</label>
                <textarea
                        id="reply_content"
                        class="form-control markitup"
                        rows="10"
                        placeholder="Content"
                        name="reply_content"
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