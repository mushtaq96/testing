using System;

using System.Collections.Generic;
using Lib.Ext.DateTime;
using System.Linq;

namespace OrderEdit.Schema
{
    public class FindKeys
    {
        public string ClientName { get; set; }
        public string StaffName { get; set; }
        public string CustomerName { get; set; }
        public string OrdId { get; set; }
    }

    public enum RowType 
    {
        New,
        Editing,
        Duplicating
    }

    /// <summary>
    /// 日付検査に関する静的クラス
    /// </summary>
    public static class DateValidations
    {
        /// <summary>
        /// 有効な年か判定する (nullの場合はTrueが返る nullチェックは別でやってね)
        /// </summary>
        /// <param name="pSelf"></param>
        /// <returns></returns>
        public static bool IsValidYear(DateTime? dateVal)
        {
            if (dateVal.HasValue)
            {
                return DateValidations.IsValidYear(dateVal.Value);
            }
            else
            {
                return true;
            }
        }

        /// <summary>
        /// 有効な年か判定する(昭和1年～2999年までの間か判定する)
        /// </summary>
        /// <param name="pSelf"></param>
        /// <returns></returns>
        public static bool IsValidYear(DateTime dateVal)
        {
            var year = dateVal.Year;
            return (year >= 1926 && year <= 2999);
        }

    }
}
