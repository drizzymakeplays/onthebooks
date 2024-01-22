# from queries.pool import pool
# from typing import List, Union
# from models.appointments import Error, AppointmentIn, AppointmentOut


# class AppointmentQueries:
#     def get_all(self) -> Union[Error, List[AppointmentOut]]:
#         try:
#             with pool.connection() as conn:
#                 with conn.cursor() as db:
#                     db.execute(
#                         """
#                         SELECT
#                             id,
#                             patient_id,
#                             hcp_id,
#                             appt_date,
#                             appt_time,
#                             appt_reason,
#                             status
#                         FROM appointments
#                         ORDER BY appt_date;
#                         """
#                     )
#                     return [
#                         AppointmentOut(
#                             id=apt[0],
#                             account_id=apt[1],
#                             appt_date=apt[2],
#                             appt_time=apt[3],
#                             appt_reason=apt[4],
#                             status=apt[5],
#                         )
#                         for apt in db
#                     ]
#         except Exception:
#             return {"message": "Could not return all appointments"}

#     def create(self, apt: AppointmentIn):
#         with pool.connection() as conn:
#             with conn.cursor() as db:
#                 params = [
#                     apt.patient_id,
#                     apt.hcp_id,
#                     apt.appt_date,
#                     apt.appt_time,
#                     apt.appt_reason,
#                     apt.status,
#                 ]
#                 db.execute(
#                     """
#                     INSERT INTO appointments
#                         (
#                             patient_id,
#                             hcp_id,
#                             appt_date,
#                             appt_time,
#                             appt_reason,
#                             status
#                         )
#                     VALUES
#                         (%s, %s, %s, %s, %s, %s)
#                     RETURNING
#                         id,
#                         patient_id,
#                         hcp_id,
#                         appt_date,
#                         appt_time,
#                         appt_reason,
#                         status
#                     ;
#                     """,
#                     params,
#                 )

#                 record = None
#                 row = db.fetchone()
#                 if row is not None:
#                     record = {}
#                     for i, col in enumerate(db.description):
#                         record[col[0]] = row[i]
#                 return AppointmentOut(**record)
