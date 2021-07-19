from flask import Flask, jsonify, request
from flask_restx import Api, Resource
from shared.db import DB
from shared.entities import HistoryRecord
from shared.utils import row_to_dict
from sqlalchemy.orm import scoped_session

app = Flask(__name__)
db = DB()
db_session = scoped_session(db.session)
api = Api(app, title="Courses api", description="Courses api")
default_namespace = api.namespace("history_date")


@app.teardown_appcontext
def shutdown_session(exception=None):
    db_session.remove()


@default_namespace.route("/filter_by_attributes")
@default_namespace.doc(
    params=dict(
        company_name="PD",
        limit="0",
        offset="0",
        # start_date='20-05-2021', end_date='20-05-2021'
    )
)
class GetCourse(Resource):
    @staticmethod
    # todo implement filter by dates
    def get():
        args = request.args
        # try:
        #     start_date_filter = datetime.strptime(args["start_date"], date_format).date()
        # except:
        #     start_date_filter = 0
        # try:
        #     end_date_filter = datetime.strptime(args["end_date"], date_format).date()
        # except:
        #     end_date_filter = 0
        # user can pass empty string or no attribute
        company_name = args.get("company_name")
        # delta = end_date_filter - start_date_filter
        # full_filter = and_()
        # filters = []
        filtered_rows = db_session.query(HistoryRecord)
        if company_name:
            filtered_rows = filtered_rows.filter_by(company_name=company_name)
        # if delta:
        #     for i in (range(delta.days + 1))[1:]:
        #         day = (start_date_filter + timedelta(days=i))
        #         delta_filter = and_(Course.end_date >= day, Course.start_date <= day, id_title_filter)
        #         filters.append(delta_filter)
        # else:
        #     filters.append(id_title_filter)
        if args.get("limit"):
            filtered_rows = filtered_rows.limit(args["limit"])
        if args.get("offset"):
            filtered_rows = filtered_rows.offset(args["offset"])
        filtered_rows = filtered_rows.all()
        response = list(map(row_to_dict, filtered_rows))
        return jsonify(response)


if __name__ == "__main__":
    app.run()
