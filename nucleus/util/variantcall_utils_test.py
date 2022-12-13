# Copyright 2018 Google LLC.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

"""Tests for variantcall_utils."""

from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import functools

from absl.testing import absltest
from absl.testing import parameterized
import mock

from nucleus.protos import struct_pb2
from nucleus.protos import variants_pb2
from nucleus.util import struct_utils
from nucleus.util import variantcall_utils




class VariantcallUtilsTests(parameterized.TestCase):

  def _assert_struct_lists_equal(self, actual, expected):
    self.assertEqual(len(actual), len(expected))
    for actual_elem, expected_elem in zip(actual, expected):
      self.assertEqual(actual_elem, expected_elem)

  @parameterized.parameters(
      dict(
          field_name='GP',
          value=[.1, .2, .7],
          reader=None,
          expected=[struct_pb2.Value(number_value=v) for v in [.1, .2, .7]]),
      dict(
          field_name='AD',
          value=[23],
          reader=None,
          expected=[struct_pb2.Value(int_value=23)]),
      dict(
          field_name='FT',
          value=['PASS'],
          reader=None,
          expected=[struct_pb2.Value(string_value='PASS')]),
      dict(
          field_name='FT',
          value=['PASS'],
          reader=True,
          expected=[struct_pb2.Value(string_value='PASS')]),
  )
  def test_set_format(self, field_name, value, reader, expected):
    if reader is not None:
      reader = mock.Mock()
      reader.field_access_cache.format_field_set_fn.return_value = (
          struct_utils.set_string_field)
    call = variants_pb2.VariantCall()
    variantcall_utils.set_format(call, field_name, value, reader)
    actual = call.info[field_name].values
    self._assert_struct_lists_equal(actual, expected)

  @parameterized.parameters(
      dict(field_name='GP', reader=None, expected=[.1, .2, .7]),
      dict(field_name='AD', reader=None, expected=[55, 3]),
      dict(field_name='DP', reader=None, expected=58),
      dict(field_name='GL', reader=None, expected=[-1, -3, -5.5]),
      dict(field_name='GT', reader=None, expected=[0, 1]),
      dict(field_name='FT', reader=None, expected='LowQual'),
      dict(field_name='FT', reader=True, expected='LowQual'),
  )
  def test_get_format(self, field_name, reader, expected):
    if reader is not None:
      reader = mock.Mock()
      reader.field_access_cache.format_field_get_fn.return_value = (
          functools.partial(
              struct_utils.get_string_field, is_single_field=True))

    call = variants_pb2.VariantCall()
    variantcall_utils.set_format(call, 'GP', [.1, .2, .7])
    variantcall_utils.set_format(call, 'AD', [55, 3])
    variantcall_utils.set_format(call, 'DP', 58)
    variantcall_utils.set_format(call, 'GL', [-1, -3, -5.5])
    variantcall_utils.set_format(call, 'GT', [0, 1])
    variantcall_utils.set_format(call, 'FT', ['LowQual'])
    actual = variantcall_utils.get_format(call, field_name, vcf_object=reader)
    self.assertEqual(actual, expected)

  @parameterized.parameters(
      dict(
          field_name='AD',
          setter=variantcall_utils.set_ad,
          getter=variantcall_utils.get_ad,
          values=[[1, 5], [30, 29]]),
      dict(
          field_name='GL',
          setter=variantcall_utils.set_gl,
          getter=variantcall_utils.get_gl,
          values=[[-1, -2, -3.3], [-0.001, -3, -10]]),
      dict(
          field_name='GQ',
          setter=variantcall_utils.set_gq,
          getter=variantcall_utils.get_gq,
          values=range(10)),
      dict(
          field_name='GT',
          setter=variantcall_utils.set_gt,
          getter=variantcall_utils.get_gt,
          values=[[0, 1], [1, 1], [1, 2]]),
      dict(
          field_name='MIN_DP',
          setter=variantcall_utils.set_min_dp,
          getter=variantcall_utils.get_min_dp,
          values=range(10)),
      dict(
          field_name='MED_DP',
          setter=variantcall_utils.set_med_dp,
          getter=variantcall_utils.get_med_dp,
          values=range(10)),
  )
  def test_variantcall_format_roundtrip(self, field_name, setter, getter,
                                        values):
    vc = variants_pb2.VariantCall()
    self.assertNotIn(field_name, vc.info)
    for value in values:
      setter(vc, value)
      if field_name not in ['GT', 'GL']:
        self.assertIn(field_name, vc.info)
      actual = getter(vc)
      self.assertEqual(actual, value)

  @parameterized.parameters(
      dict(genotype=[], expected=False),
      dict(genotype=[-1], expected=False),
      dict(genotype=[-1, -1], expected=False),
      dict(genotype=[-1, -1073741825], expected=False),
      dict(genotype=[-1, 0], expected=True),
      dict(genotype=[0, 0], expected=True),
      dict(genotype=[0, 1], expected=True),
      dict(genotype=[0, 1, -1], expected=True),
      dict(genotype=[-1, 0, -1073741825], expected=True),
  )
  def test_has_genotypes(self, genotype, expected):
    call = variants_pb2.VariantCall(genotype=genotype)
    actual = variantcall_utils.has_genotypes(call)
    self.assertEqual(actual, expected)

  @parameterized.parameters(
      dict(genotype=[], expected=True),
      dict(genotype=[-1], expected=False),
      dict(genotype=[-1, -1073741825], expected=False),
      dict(genotype=[-1, 0], expected=False),
      dict(genotype=[0, 0], expected=True),
      dict(genotype=[0, 1], expected=True),
      dict(genotype=[0, 1, -1], expected=False),
      dict(genotype=[1, 0, -1073741825], expected=False),
  )
  def test_has_full_genotypes(self, genotype, expected):
    call = variants_pb2.VariantCall(genotype=genotype)
    actual = variantcall_utils.has_full_genotypes(call)
    self.assertEqual(actual, expected)

  @parameterized.parameters(
      dict(genotype=[], expected=0),
      dict(genotype=[-1], expected=1),
      dict(genotype=[-1, -1], expected=2),
      dict(genotype=[-1, -1073741825], expected=1),
      dict(genotype=[-1, 0], expected=2),
      dict(genotype=[0, 0], expected=2),
      dict(genotype=[0, 1], expected=2),
      dict(genotype=[0, 1, -1], expected=3),
      dict(genotype=[-1, 0, -1073741825], expected=2),
  )
  def test_ploidy(self, genotype, expected):
    call = variants_pb2.VariantCall(genotype=genotype)
    actual = variantcall_utils.ploidy(call)
    self.assertEqual(actual, expected)

  @parameterized.parameters(
      dict(genotype=[], expected=False),
      dict(genotype=[-1], expected=False),
      dict(genotype=[-1, -1], expected=False),
      dict(genotype=[-1, -1073741825], expected=False),
      dict(genotype=[-1, 0], expected=False),
      dict(genotype=[0, 0], expected=False),
      dict(genotype=[0, 1], expected=True),
      dict(genotype=[0, 1, -1], expected=True),
      dict(genotype=[-1, 0, -1073741825], expected=False),
  )
  def test_has_variation(self, genotype, expected):
    call = variants_pb2.VariantCall(genotype=genotype)
    actual = variantcall_utils.has_variation(call)
    self.assertEqual(actual, expected)

  @parameterized.parameters(
      dict(genotype=[], expected=False),
      dict(genotype=[-1], expected=False),
      dict(genotype=[-1, -1], expected=False),
      dict(genotype=[-1, -1073741825], expected=False),
      dict(genotype=[-1, 0], expected=False),
      dict(genotype=[0, 0], expected=False),
      dict(genotype=[0, 1], expected=True),
      dict(genotype=[0, 2], expected=True),
      dict(genotype=[1, 1], expected=False),
      dict(genotype=[2, 2], expected=False),
      dict(genotype=[1, 2], expected=True),
      dict(genotype=[0, 1, -1], expected=True),
      dict(genotype=[0, 1, 2], expected=True),
      dict(genotype=[-1, 0, -1073741825], expected=False),
  )
  def test_is_heterozygous(self, genotype, expected):
    call = variants_pb2.VariantCall(genotype=genotype)
    actual = variantcall_utils.is_heterozygous(call)
    self.assertEqual(actual, expected)


if __name__ == '__main__':
  absltest.main()
